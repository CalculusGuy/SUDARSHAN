# reporter/poc_generator.py
import os
from datetime import datetime

def generate_poc(findings, target, output_dir="pocs"):
    """
    Generate proof-of-concept scripts for each confirmed finding.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    poc_files = []
    
    for finding in findings:
        # Skip if finding is not a dict
        if not isinstance(finding, dict):
            continue
            
        # Only generate PoC for confirmed findings
        if not finding.get("confirmed", False):
            continue
            
        rule_name = finding.get("rule", "Unknown")
        rule_id = finding.get("rule_id", "unknown")
        payload = finding.get("payload", "")
        parameter = finding.get("parameter", "id")
        indicator = finding.get("indicator", "")
        url = finding.get("url", target)
        severity = finding.get("severity", "Medium")
        cwe = finding.get("cwe", "N/A")
        
        # Build the PoC script
        code = f'''#!/usr/bin/env python3
# PoC for {rule_name}
# Severity: {severity}
# CWE: {cwe}
# Generated: {datetime.now().isoformat()}
# Target: {target}

import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit():
    target = "{url}"
    payload = "{payload}"
    params = {{"{parameter}": payload}}
    
    try:
        response = requests.get(target, params=params, timeout=10, verify=False)
        print(f"Status: {{response.status_code}}")
        if "{indicator}".lower() in response.text.lower():
            print("[!] Vulnerability confirmed!")
            return True
        else:
            print("[+] No vulnerability detected.")
            return False
    except Exception as e:
        print(f"[-] Error: {{e}}")
        return False

if __name__ == "__main__":
    exploit()
'''
        
        filename = f"{output_dir}/poc_{rule_id}.py"
        with open(filename, "w", encoding='utf-8') as f:
            f.write(code)
        
        poc_files.append(filename)
    
    return poc_files
