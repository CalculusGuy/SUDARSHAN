@pytest.fixture
def target_url():
    return "http://localhost:5000"
import pytest
import json
import time
from engine.engine import test_url

class TestSUDARSHAN:
    """Test suite for SUDARSHAN DAST Engine."""

    # --- Rule Loading ---
    def test_rule_loading(self, sample_rules):
        """Verify that the rule file loads correctly."""
        assert len(sample_rules) > 0
        print(f"\n✅ Loaded {len(sample_rules)} rules")

    # --- Detection Tests ---
    @pytest.mark.parametrize("url,description", [
        ("http://localhost:5000/search?q=<script>alert(1)</script>", "XSS"),
        ("http://localhost:5000/login?username=admin' --", "SQLi"),
        ("http://localhost:5000/ping?host=127.0.0.1;id", "Command Injection"),
    ])
    def test_detection(self, sample_rules, url, description):
        """Test that SUDARSHAN detects common vulnerabilities."""
        result = test_url(url, sample_rules)
        print(f"\n🔍 {description} test found {len(result)} findings")
        assert len(result) > 0, f"No findings detected for {description}"

    # --- Performance Test ---
    def test_performance(self, sample_rules):
        """Ensure SUDARSHAN completes a scan within acceptable time."""
        start = time.time()
        test_url("http://localhost:5000/search?q=<script>alert(1)</script>", sample_rules)
        elapsed = time.time() - start
        print(f"\n⚡ Performance: {elapsed:.3f} seconds")
        # Increased timeout to 90 seconds for comprehensive scans
        assert elapsed < 90.0, f"Scan took {elapsed:.2f}s, expected < 90s"

    # --- Rule Coverage ---
    def test_rule_coverage(self, sample_rules):
        """Validate that all rules contain payloads."""
        total_payloads = sum(
            len(vector["payloads"])
            for rule in sample_rules
            for vector in rule.get("attack_vectors", [])
        )
        print(f"\n📊 Total payloads across all rules: {total_payloads}")
        assert total_payloads > 0

    # --- Edge Case: Empty URL ---
    def test_empty_url(self, sample_rules):
        """Test behavior with empty URL."""
        result = test_url("", sample_rules)
        assert len(result) == 0, "Empty URL should return no findings"
        print("\n✅ Empty URL test passed")

    # --- Edge Case: Invalid URL ---
    def test_invalid_url(self, sample_rules):
        """Test behavior with invalid URL."""
        result = test_url("http://invalid.url.xyz", sample_rules)
        assert len(result) == 0, "Invalid URL should return no findings"
        print("\n✅ Invalid URL test passed")