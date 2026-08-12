# engine/engine.py
import requests
# engine/engine.py
from urllib.parse import urljoin  # <--- ADD THIS LINE

def test_url(target_url, rules):
    findings = []
    for rule in rules:
        for vector in rule["attack_vectors"]:
            method = vector.get("method", "GET")
            param = vector.get("parameter", "id")
            for payload in vector.get("payloads", []):
                if "?" in target_url:
                    attack_url = target_url + f"&{param}={payload}"
                else:
                    attack_url = target_url + f"?{param}={payload}"
                try:
                    if method.upper() == "GET":
                        response = requests.get(attack_url, timeout=5)
                    else:
                        response = requests.get(attack_url, timeout=5, verify=False)
                    for indicator in rule["detection"].get("response_indicators", []):
                        if indicator.lower() in response.text.lower():
                            findings.append({
                                "rule": rule["name"],
                                "severity": rule.get("severity", "Medium"),
                                "payload": payload,
                                "url": attack_url,
                                "indicator": indicator
                            })
                            print(f"  [!] {rule['name']} found! Payload: {payload}")
                except Exception as e:
                    print(f"  [x] Error: {e}")
    return findings

def test_form(form, rules, base_url):
    findings = []
    form_action = form["action"]
    form_method = form["method"]

    if form_action.startswith("/"):
        form_action = urljoin(base_url, form_action)

    if not form_action.startswith("http"):
        return findings

    for rule in rules:
        for vector in rule["attack_vectors"]:
            for payload in vector.get("payloads", []):
                form_data = {input_name: payload for input_name in form["inputs"]}
                try:
                    if form_method == "GET":
                        response = requests.get(form_action, params=form_data, timeout=5)
                    else:
                        response = requests.post(form_action, data=form_data, timeout=5)
                    for indicator in rule["detection"].get("response_indicators", []):
                        if indicator.lower() in response.text.lower():
                            findings.append({
                                "rule": rule["name"],
                                "severity": rule.get("severity", "Medium"),
                                "payload": payload,
                                "url": form_action,
                                "indicator": indicator
                            })
                            print(f"  [!] {rule['name']} found in form! Payload: {payload}")
                except Exception as e:
                    print(f"  [x] Error testing form: {e}")
    return findings
