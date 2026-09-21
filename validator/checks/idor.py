# validator/checks/idor.py
"""
IDOR Validator — differential comparison across object references.
"""

import requests
import urllib3
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
from ..result import ValidationResult

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _replace_param(url: str, param: str, value: str) -> str:
    """Replace a query parameter value in a URL."""
    parts = urlsplit(url)
    q = dict(parse_qsl(parts.query, keep_blank_values=True))
    q[param] = value
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(q), parts.fragment))


def validate_idor(finding: dict, timeout: int = 10, verify: bool = False) -> ValidationResult:
    """
    Validate IDOR by comparing responses across different object references.
    """
    url = finding.get("url", "")
    parameter = finding.get("parameter", "")

    if not url or not parameter:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="IDOR",
            url=url,
            parameter=parameter,
            evidence=["URL or parameter missing"],
        )

    # --- Fetch original response ---
    try:
        orig_resp = requests.get(url, timeout=timeout, verify=verify)
        orig_text = orig_resp.text
        orig_len = len(orig_text)
    except Exception as e:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="IDOR",
            url=url,
            parameter=parameter,
            evidence=[f"Failed to fetch original: {str(e)[:100]}"],
        )

    # --- Fetch a different object reference ---
    alt_url = _replace_param(url, parameter, "2")
    try:
        alt_resp = requests.get(alt_url, timeout=timeout, verify=verify)
        alt_text = alt_resp.text
        alt_len = len(alt_text)
    except Exception as e:
        return ValidationResult(
            status="ERROR",
            confidence=0,
            vulnerability="IDOR",
            url=url,
            parameter=parameter,
            evidence=[f"Failed to fetch alternative: {str(e)[:100]}"],
        )

    # --- Compare ---
    if orig_text == alt_text:
        return ValidationResult(
            status="UNVERIFIED",
            confidence=0,
            vulnerability="IDOR",
            url=url,
            parameter=parameter,
            evidence=["Responses are identical — no IDOR evidence"],
        )

    # Significant size difference = strong signal
    if alt_len > orig_len * 1.2 or orig_len > alt_len * 1.2:
        return ValidationResult(
            status="CONFIRMED",
            confidence=75,
            vulnerability="IDOR",
            url=url,
            parameter=parameter,
            evidence=[f"Response size differs significantly ({orig_len} vs {alt_len})"],
            poc_command=f"curl '{alt_url}'",
            poc_response=alt_text[:500],
        )

    return ValidationResult(
        status="UNVERIFIED",
        confidence=10,
        vulnerability="IDOR",
        url=url,
        parameter=parameter,
        evidence=["Minor differences detected — manual review recommended"],
    )