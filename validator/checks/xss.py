# validator/checks/xss.py
"""XSS (Cross-Site Scripting) Validator."""

import html
import uuid
import re
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode
from ..result import ValidationResult
from ..http_client import SafeHTTPClient


def build_clean_url(url, parameter, value):
    """Build a URL with a clean parameter value."""
    # If URL already has ? and the parameter, replace it
    if '?' in url and f'{parameter}=' in url:
        # Find the parameter and replace its value
        pattern = rf'{parameter}=[^&]*'
        new_url = re.sub(pattern, f'{parameter}={value}', url)
        return new_url
    else:
        # Simple case: just add the parameter
        if '?' in url:
            return f'{url}&{parameter}={value}'
        else:
            return f'{url}?{parameter}={value}'


def validate_xss(finding: dict, timeout: int = 10, verify: bool = False) -> ValidationResult:
    """
    Validate XSS findings.
    
    Step 1: Inject a unique marker
    Step 2: Check if marker is reflected in response
    Step 3: Check if marker is HTML-escaped
    Step 4: Return CONFIRMED or UNVERIFIED with confidence
    """
    
    url = finding.get("url", "")
    parameter = finding.get("parameter", "q")
    
    if not url:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="Cross-Site Scripting",
            url="",
            parameter=parameter,
            evidence=["No URL provided"]
        )
    
    client = SafeHTTPClient(timeout=timeout, verify=verify)
    evidence = []
    details = {}
    
    # Generate a unique marker
    marker = "SUDARSHAN-" + uuid.uuid4().hex[:12]
    
    try:
        # Step 1: Baseline request (no payload)
        baseline_url = build_clean_url(url, parameter, "test")
        baseline_response = client.get(baseline_url)
        
        evidence.append(f"✅ Baseline captured: {len(baseline_response.text)} bytes")
        
        # Step 2: Attack request with marker
        attack_url = build_clean_url(url, parameter, marker)
        attack_response = client.get(attack_url)
        body = attack_response.text
        
        # Step 3: Check if marker is reflected
        if marker not in body:
            return ValidationResult(
                status="UNVERIFIED",
                confidence=5,
                vulnerability="Cross-Site Scripting",
                url=url,
                parameter=parameter,
                evidence=evidence + ["❌ Marker was not reflected in response"],
                details={"marker": marker}
            )
        
        evidence.append(f"✅ Marker reflected: {marker}")
        
        # Step 4: Check if marker is HTML-escaped
        # CORRECT: Check if the marker appears as HTML entities
        # e.g., &lt;script&gt; vs <script>
        marker_escaped = html.escape(marker)
        
        # Check if the escaped version appears in the body
        if marker_escaped in body and marker not in body:
            evidence.append("⚠️ Marker is HTML-escaped (likely not exploitable)")
            confidence = 30
            status = "UNVERIFIED"
        else:
            # Check if the original marker appears (not escaped)
            if marker in body:
                evidence.append("✅ Marker is NOT HTML-escaped (potential XSS)")
                confidence = 80
                status = "CONFIRMED"
                
                # Build PoC command
                script_payload = "<script>alert(1)</script>"
                poc_url = build_clean_url(url, parameter, script_payload)
                poc_command = f'curl "{poc_url}"'
                details["poc_command"] = poc_command
                
                # Test with a simple script
                script_response = client.get(poc_url)
                
                if "<script>alert(1)</script>" in script_response.text:
                    evidence.append("✅ Script payload reflected (CONFIRMED XSS)")
                    confidence = 95
                    details["script_reflected"] = True
                    details["poc_response"] = script_response.text[:200]
                else:
                    evidence.append("⚠️ Script payload not fully reflected")
                    confidence = 70
        
        return ValidationResult(
            status=status,
            confidence=confidence,
            vulnerability="Cross-Site Scripting",
            url=url,
            parameter=parameter,
            evidence=evidence,
            details=details,
            poc_command=details.get("poc_command", "")
        )
        
    except Exception as e:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="Cross-Site Scripting",
            url=url,
            parameter=parameter,
            evidence=[f"Validation error: {str(e)[:100]}"]
        )