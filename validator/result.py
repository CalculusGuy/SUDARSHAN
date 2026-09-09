# validator/result.py
from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class ValidationResult:
    """Validation result for a single finding."""
    
    status: str  # CONFIRMED, UNVERIFIED, ERROR
    confidence: int  # 0-100
    vulnerability: str
    url: str
    parameter: Optional[str] = None
    evidence: List[str] = field(default_factory=list)
    details: dict = field(default_factory=dict)
    poc_command: Optional[str] = None
    poc_response: Optional[str] = None
    
    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "confidence": self.confidence,
            "vulnerability": self.vulnerability,
            "url": self.url,
            "parameter": self.parameter,
            "evidence": self.evidence,
            "details": self.details,
            "poc_command": self.poc_command,
            "poc_response": self.poc_response
        }
    
    def is_confirmed(self) -> bool:
        return self.status == "CONFIRMED"
    
    def is_unverified(self) -> bool:
        return self.status == "UNVERIFIED"