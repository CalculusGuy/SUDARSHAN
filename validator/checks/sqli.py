# validator/checks/sqli.py
"""SQL Injection Validator."""

import re
from urllib.parse import quote
from ..result import ValidationResult
from ..http_client import SafeHTTPClient


def validate_sqli(finding: dict, timeout: int = 10, verify: bool = False) -> ValidationResult:
    """
    Validate SQL Injection findings.
    
    Step 1: Inject a test payload that causes a known error
    Step 2: Check for SQL error indicators
    Step 3: Return CONFIRMED or UNVERIFIED with confidence
    """
    
    url = finding.get("url", "")
    parameter = finding.get("parameter", "id")
    
    if not url:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="SQL Injection",
            url="",
            parameter=parameter,
            evidence=["No URL provided"]
        )
    
    client = SafeHTTPClient(timeout=timeout, verify=verify)
    evidence = []
    details = {}
    
    # SQL error indicators
    sql_indicators = [
        "SQL syntax",
        "mysql_fetch",
        "ORA-",
        "PostgreSQL",
        "SQLite",
        "Unclosed quotation mark",
        "Microsoft OLE DB",
        "error in your SQL",
        "near ''",
        "at line 1"
    ]
    
    # Test payloads
    test_payloads = [
        ("' OR '1'='1", "OR injection"),
        ("admin'--", "comment injection"),
        ("' AND 1=1--", "AND injection"),
    ]
    
    try:
        # Step 1: Baseline request
        baseline_params = {parameter: "test"}
        baseline_response = client.get(url, params=baseline_params)
        baseline_body = baseline_response.text
        evidence.append(f"✅ Baseline captured: {len(baseline_body)} bytes")
        
        # Step 2: Test each payload
        for payload, payload_type in test_payloads:
            # URL-encode the payload
            encoded_payload = quote(payload, safe='')
            attack_url = f"{url}?{parameter}={encoded_payload}"
            attack_response = client.get(attack_url)
            body = attack_response.text
            
            # Check for SQL error indicators
            found_indicators = []
            for indicator in sql_indicators:
                if indicator.lower() in body.lower():
                    found_indicators.append(indicator)
            
            if found_indicators:
                evidence.append(f"✅ SQL error indicators found with '{payload}'")
                evidence.append(f"   Indicators: {', '.join(found_indicators)}")
                confidence = 90
                status = "CONFIRMED"
                
                details["payload"] = payload
                details["payload_type"] = payload_type
                details["indicators"] = found_indicators
                details["poc_command"] = f'curl "{url}?{parameter}={quote(payload, safe="")}"'
                details["poc_response"] = body[:200]
                
                return ValidationResult(
                    status=status,
                    confidence=confidence,
                    vulnerability="SQL Injection",
                    url=url,
                    parameter=parameter,
                    evidence=evidence,
                    details=details,
                    poc_command=details.get("poc_command", "")
                )
        
        # If no indicators found
        evidence.append("❌ No SQL error indicators found")
        confidence = 10
        status = "UNVERIFIED"
        
        return ValidationResult(
            status=status,
            confidence=confidence,
            vulnerability="SQL Injection",
            url=url,
            parameter=parameter,
            evidence=evidence,
            details=details
        )
        
    except Exception as e:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="SQL Injection",
            url=url,
            parameter=parameter,
            evidence=[f"Validation error: {str(e)[:100]}"]
        )