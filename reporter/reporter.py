# reporter/reporter.py
import json
from datetime import datetime

def generate_json_report(findings, target_url):
    report = {
        "target": target_url,
        "scan_date": datetime.now().isoformat(),
        "total_findings": len(findings),
        "findings": findings
    }
    with open("scan_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\n[+] JSON report saved to scan_report.json")

def generate_html_report(findings, target_url):
    html = f"""
    <html>
    <head><title>DAST Scan Report</title></head>
    <body>
    <h1>DAST Scan Report</h1>
    <p><strong>Target:</strong> {target_url}</p>
    <p><strong>Scan Date:</strong> {datetime.now().isoformat()}</p>
    <p><strong>Total Findings:</strong> {len(findings)}</p>
    <ul>
    """
    for finding in findings:
        html += f"<li><strong>{finding['rule']}</strong> - {finding['severity']} - {finding['payload']}</li>"
    html += "</ul></body></html>"

    with open("scan_report.html", "w") as f:
        f.write(html)
    print("[+] HTML report saved to scan_report.html")
