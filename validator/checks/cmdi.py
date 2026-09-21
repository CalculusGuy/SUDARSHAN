# validator/checks/cmdi.py
"""
Command Injection Validator — in-band confirmation via command output.
"""

import requests
import urllib3
from ..result import ValidationResult

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Common command output indicators
INDICATORS = [
    "uid=",
    "gid=",
    "groups=",
    "root:",
    "bin:",
    "daemon:",
    "C:\\Windows",
    "nt authority",
    "volume serial number",
    "directory of",
]

def validate_cmdi(finding: dict, timeout: int = 10, verify: bool = False) -> ValidationResult:
    """
    Validate Command Injection by checking for command output
    in the payload response that is NOT present in the baseline response.
    """
    url = finding.get("url", "")
    parameter = finding.get("parameter", "")

    if not url:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="Command Injection",
            url="",
            evidence=["No URL provided"],
        )

    # --- Fetch baseline (without payload) ---
    try:
        baseline_resp = requests.get(url, timeout=timeout, verify=verify)
        baseline_text = baseline_resp.text
    except Exception as e:
        baseline_text = f"__ERROR__: {str(e)[:100]}"

    # --- Fetch payload response ---
    try:
        payload_resp = requests.get(url, timeout=timeout, verify=verify)
        payload_text = payload_resp.text
    except Exception as e:
        payload_text = f"__ERROR__: {str(e)[:100]}"

    # --- Check indicators ---
    hits = []
    for indicator in INDICATORS:
        if indicator.lower() in payload_text.lower() and indicator.lower() not in baseline_text.lower():
            hits.append(indicator)

    if hits:
        return ValidationResult(
            status="CONFIRMED",
            confidence=90,
            vulnerability="Command Injection",
            url=url,
            parameter=parameter,
            evidence=[f"Command output found: {h}" for h in hits],
            poc_command=f"curl '{url}'",
            poc_response=payload_text[:500],
        )

    return ValidationResult(
        status="UNVERIFIED",
        confidence=0,
        vulnerability="Command Injection",
        url=url,
        parameter=parameter,
        evidence=["No command output found in payload response"],
    )