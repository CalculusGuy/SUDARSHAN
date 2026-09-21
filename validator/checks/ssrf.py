# validator/checks/ssrf.py
"""
SSRF Validator — in-band confirmation via internal indicators.
"""

import requests
import urllib3
from ..result import ValidationResult

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

INDICATORS = [
    "169.254.169.254",
    "127.0.0.1",
    "localhost",
    "metadata",
    "internal",
    "192.168.",
    "10.0.",
    "172.16.",
    "root:x:0:0",
    "ami-id",
    "instance-id",
]

def validate_ssrf(finding: dict, timeout: int = 10, verify: bool = False) -> ValidationResult:
    """
    Validate SSRF by checking for internal indicators in the payload response
    that are NOT present in the baseline response.
    """
    url = finding.get("url", "")
    parameter = finding.get("parameter", "")

    if not url:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="SSRF",
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
            confidence=85,
            vulnerability="SSRF",
            url=url,
            parameter=parameter,
            evidence=[f"Internal indicator found: {h}" for h in hits],
            poc_command=f"curl '{url}'",
            poc_response=payload_text[:500],
        )

    return ValidationResult(
        status="UNVERIFIED",
        confidence=0,
        vulnerability="SSRF",
        url=url,
        parameter=parameter,
        evidence=["No internal indicators found in payload response"],
    )