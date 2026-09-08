# engine/engine.py
import requests
import urllib3
from urllib.parse import urljoin, urlparse

# Disable SSL warnings globally
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_url(url, rules, timeout=5):
    """
    Test a single URL against all rules.
    """
    findings = []
    
    for rule in rules:
        for vector in rule.get("attack_vectors", []):
            if vector.get("method", "GET").upper() != "GET":
                continue
            
            parameter = vector.get("parameter", "id")
            for payload in vector.get("payloads", []):
                try:
                    # Build attack URL with payload
                    attack_url = inject_payload(url, parameter, payload)
                    
                    # Send request with SSL verification disabled
                    response = requests.get(attack_url, timeout=timeout, verify=False)
                    
                    # Check for indicators
                    indicators = rule.get("detection", {}).get("response_indicators", [])
                    for indicator in indicators:
                        if indicator.lower() in response.text.lower():
                            findings.append({
                                "rule": rule.get("name", "Unknown"),
                                "rule_id": rule.get("rule_id", "N/A"),
                                "severity": rule.get("severity", "Medium"),
                                "cwe": rule.get("cwe", "N/A"),
                                "payload": payload,
                                "parameter": parameter,
                                "url": attack_url,
                                "indicator": indicator,
                                "confirmed": True,
                                "timestamp": str(requests.get(url, timeout=timeout, verify=False).elapsed.total_seconds())
                            })
                            break
                            
                except requests.exceptions.SSLError:
                    # Skip SSL errors silently
                    continue
                except requests.exceptions.Timeout:
                    continue
                except Exception:
                    continue
    
    return findings


def test_form(form, rules, target_url, timeout=5):
    """
    Test a form against all rules.
    """
    findings = []
    
    action = form.get("action", target_url)
    method = form.get("method", "get").upper()
    inputs = form.get("inputs", [])
    
    for rule in rules:
        for vector in rule.get("attack_vectors", []):
            vector_method = vector.get("method", "GET").upper()
            if vector_method != method:
                continue
            
            parameter = vector.get("parameter", "")
            if not parameter:
                continue
            
            # Check if the parameter exists in the form
            param_exists = any(inp.get("name") == parameter for inp in inputs)
            if not param_exists:
                continue
            
            for payload in vector.get("payloads", []):
                try:
                    # Build form data with payload
                    data = {}
                    for inp in inputs:
                        if inp.get("name") == parameter:
                            data[inp.get("name")] = payload
                        else:
                            data[inp.get("name")] = "test123"
                    
                    # Send request with SSL verification disabled
                    if method == "POST":
                        response = requests.post(action, data=data, timeout=timeout, verify=False)
                    else:
                        response = requests.get(action, params=data, timeout=timeout, verify=False)
                    
                    # Check for indicators
                    indicators = rule.get("detection", {}).get("response_indicators", [])
                    for indicator in indicators:
                        if indicator.lower() in response.text.lower():
                            findings.append({
                                "rule": rule.get("name", "Unknown"),
                                "rule_id": rule.get("rule_id", "N/A"),
                                "severity": rule.get("severity", "Medium"),
                                "cwe": rule.get("cwe", "N/A"),
                                "payload": payload,
                                "parameter": parameter,
                                "url": action,
                                "indicator": indicator,
                                "confirmed": True,
                                "timestamp": str(response.elapsed.total_seconds())
                            })
                            break
                            
                except requests.exceptions.SSLError:
                    continue
                except requests.exceptions.Timeout:
                    continue
                except Exception:
                    continue
    
    return findings


def inject_payload(url, parameter, payload):
    """
    Inject a payload into a URL parameter.
    """
    parsed = urlparse(url)
    query = parsed.query
    
    if query:
        # Replace or add the parameter
        params = {}
        for param in query.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                params[key] = value
        params[parameter] = payload
        
        # Rebuild query string
        new_query = '&'.join([f"{k}={v}" for k, v in params.items()])
        return urljoin(url, f"{parsed.path}?{new_query}")
    else:
        return urljoin(url, f"{parsed.path}?{parameter}={payload}")
