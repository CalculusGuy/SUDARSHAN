# main.py
import json
from crawler.crawler import crawl
from engine.engine import test_url, test_form
from reporter.reporter import generate_json_report, generate_html_report

def load_rules():
    with open("dast_rules.json", "r") as f:
        data = json.load(f)
    return data["rules"]

def main():
    print("\n" + "="*50)
    print("DAST ENGINE v2.0")
    print("Dynamic Application Security Testing Tool")
    print("="*50 + "\n")

    rules = load_rules()
    target = input("Enter target URL: ")

    print(f"\n[*] Scanning: {target}")
    pages, forms = crawl(target, max_pages=10)
    print(f"[+] Found {len(pages)} pages, {len(forms)} forms")

    findings = []
    for page in pages[:3]:
        findings.extend(test_url(page, rules))
    for form in forms[:3]:
        findings.extend(test_form(form, rules, target))

    generate_json_report(findings, target)
    generate_html_report(findings, target)
    print(f"\n[+] Scan complete. Found {len(findings)} vulnerabilities.")

if __name__ == "__main__":
    main()
