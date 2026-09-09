"""
Response Differential Analyzer for SUDARSHAN v2.0
Replaces broken string-matching with intelligent baseline comparison
"""

import difflib
import time
from typing import Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class ResponsePair:
    """Container for baseline and attack responses"""
    baseline_status: int
    attack_status: int
    baseline_body: str
    attack_body: str
    baseline_headers: dict
    attack_headers: dict
    baseline_time: float
    attack_time: float
    baseline_size: int
    attack_size: int

class DiffAnalyzer:
    """Analyzes differences between baseline and attack responses"""
    
    @staticmethod
    def calculate_similarity(text1: str, text2: str) -> float:
        """Return similarity score between two strings (0.0 to 1.0)"""
        if not text1 and not text2:
            return 1.0
        if not text1 or not text2:
            return 0.0
        return difflib.SequenceMatcher(None, text1, text2).ratio()
    
    @staticmethod
    def analyze(resp_pair: ResponsePair) -> Dict:
        """
        Perform multi-signal differential analysis
        Returns: {
            'confidence': float (0-100),
            'signals': dict of individual signal scores,
            'reasoning': str
        }
        """
        signals = {}
        
        # Signal 1: Body similarity delta
        similarity = DiffAnalyzer.calculate_similarity(
            resp_pair.baseline_body, 
            resp_pair.attack_body
        )
        signals['body_delta'] = (1 - similarity) * 100
        # Higher delta = more suspicious
        
        # Signal 2: Status code change
        signals['status_delta'] = 100 if resp_pair.baseline_status != resp_pair.attack_status else 0
        # 200->500 = 100%, 200->404 = 80%, 200->200 = 0%
        if resp_pair.baseline_status == 200 and resp_pair.attack_status in [500, 502, 503]:
            signals['status_delta'] = 100
        elif resp_pair.baseline_status != resp_pair.attack_status:
            signals['status_delta'] = 80
        
        # Signal 3: Response size delta
        if resp_pair.baseline_size > 0:
            size_ratio = resp_pair.attack_size / resp_pair.baseline_size
            if size_ratio > 3 or size_ratio < 0.3:
                signals['size_delta'] = 100
            elif size_ratio > 2 or size_ratio < 0.5:
                signals['size_delta'] = 70
            elif size_ratio > 1.5 or size_ratio < 0.6:
                signals['size_delta'] = 40
            else:
                signals['size_delta'] = 0
        else:
            signals['size_delta'] = 0
        
        # Signal 4: Timing delta (for time-based attacks)
        time_diff = resp_pair.attack_time - resp_pair.baseline_time
        if time_diff > 4.0:  # 4+ seconds delay
            signals['time_delta'] = 100
        elif time_diff > 2.0:
            signals['time_delta'] = 70
        elif time_diff > 1.0:
            signals['time_delta'] = 40
        else:
            signals['time_delta'] = 0
        
        # Signal 5: Header changes
        baseline_keys = set(resp_pair.baseline_headers.keys())
        attack_keys = set(resp_pair.attack_headers.keys())
        new_headers = attack_keys - baseline_keys
        if 'X-Sql-Error' in new_headers or 'X-Debug' in new_headers:
            signals['header_delta'] = 100
        elif new_headers:
            signals['header_delta'] = 60
        else:
            signals['header_delta'] = 0
        
        # Weighted confidence calculation
        weights = {
            'body_delta': 0.35,
            'status_delta': 0.25,
            'size_delta': 0.20,
            'time_delta': 0.10,
            'header_delta': 0.10
        }
        
        confidence = sum(signals.get(k, 0) * weights[k] for k in weights.keys())
        confidence = round(min(confidence, 100), 1)
        
        # Determine if finding is valid
        is_valid = confidence >= 50.0  # Configurable threshold
        
        # Generate reasoning
        reasoning = []
        if signals['body_delta'] > 60:
            reasoning.append(f"Significant body content change ({signals['body_delta']:.0f}%)")
        if signals['status_delta'] > 50:
            reasoning.append(f"Status code changed from {resp_pair.baseline_status} to {resp_pair.attack_status}")
        if signals['size_delta'] > 50:
            reasoning.append(f"Response size changed by {abs(resp_pair.attack_size - resp_pair.baseline_size)} bytes")
        if signals['time_delta'] > 50:
            reasoning.append(f"Response delayed by {time_diff:.2f} seconds (potential time-based vulnerability)")
        if signals['header_delta'] > 50:
            reasoning.append(f"New response headers detected: {list(new_headers)}")
        
        return {
            'confidence': confidence,
            'is_valid': is_valid,
            'signals': signals,
            'reasoning': '; '.join(reasoning) if reasoning else 'Minimal differential changes detected'
        }
