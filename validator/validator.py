# validator/validator.py
"""
FindingValidator - Dispatches findings to the appropriate validator.
"""

from .result import ValidationResult

# Import validators (they will be defined in checks/)
from .checks.ssti import validate_ssti
from .checks.sqli import validate_sqli
from .checks.xss import validate_xss


# Map vulnerability names to validator functions
VALIDATORS = {
    # SSTI
    "Server-Side Template Injection (SSTI)": validate_ssti,
    "SSTI": validate_ssti,
    "Template Injection": validate_ssti,
    
    # SQL Injection
    "SQL Injection": validate_sqli,
    "SQLi": validate_sqli,
    "SQL Injection Detection": validate_sqli,
    
    # XSS
    "Cross-Site Scripting": validate_xss,
    "XSS": validate_xss,
    "Cross-Site Scripting (XSS) Detection": validate_xss,
}


class FindingValidator:
    """
    Validates findings from SUDARSHAN scanner.
    Returns CONFIRMED, UNVERIFIED, or ERROR status with confidence score.
    """
    
    def __init__(self, timeout: int = 10, verify: bool = False):
        self.timeout = timeout
        self.verify = verify
    
    def validate(self, finding: dict) -> ValidationResult:
        """
        Validate a single finding.
        
        Args:
            finding: Dictionary with fields:
                - vulnerability: str
                - url: str
                - parameter: str (optional)
                - method: str (optional)
                - evidence: str (optional)
        
        Returns:
            ValidationResult
        """
        
        vulnerability = finding.get("vulnerability", "")
        
        # Find matching validator
        validator = None
        for key in VALIDATORS:
            if key.lower() in vulnerability.lower() or vulnerability.lower() in key.lower():
                validator = VALIDATORS[key]
                break
        
        if not validator:
            return ValidationResult(
                status="UNVERIFIED",
                confidence=0,
                vulnerability=vulnerability,
                url=finding.get("url", ""),
                parameter=finding.get("parameter"),
                evidence=["No dedicated validator available for this vulnerability type"]
            )
        
        # Run the validator
        try:
            return validator(finding, timeout=self.timeout, verify=self.verify)
        except Exception as e:
            return ValidationResult(
                status="ERROR",
                confidence=0,
                vulnerability=vulnerability,
                url=finding.get("url", ""),
                parameter=finding.get("parameter"),
                evidence=[f"Validator error: {str(e)[:100]}"]
            )
    
    def validate_all(self, findings: list) -> list:
        """Validate a list of findings."""
        results = []
        for finding in findings:
            result = self.validate(finding)
            results.append(result)
        return results