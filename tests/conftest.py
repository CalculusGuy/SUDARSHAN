import pytest
import json
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture
def sample_rules():
    with open("rules/dast_rules.json", "r") as f:
        return json.load(f)["rules"]
