SUDARSHAN
Enterprise DAST Engine for Modern Web Applications

Cuts through web vulnerabilities.

Show Image Show Image Show Image Show Image

</div>
Overview

SUDARSHAN is a modular Dynamic Application Security Testing (DAST) engine built to discover and report web application vulnerabilities at scale. It crawls a target application, launches configurable attack payloads against every discovered URL and form, and produces both machine-readable and human-readable vulnerability reports — all wrapped in a hacker-styled terminal UI.

Named after the discus of Vishnu — a weapon that cuts through anything in its path — SUDARSHAN is built to slice through the attack surface of modern web apps.

⚠️ For authorized security testing only. Only scan applications you own or have explicit written permission to test. See Legal & Ethical Use.

Features
Capability	Description
🕷️ Modular Architecture	Independent crawler, engine, and reporter components — swap or extend any layer
📜 Rule-Based Detection	Vulnerability checks defined declaratively in rules/dast_rules.json
📊 Multi-Format Reporting	Auto-generated JSON (machine-readable) and HTML (human-readable) reports
🖥️ Hacker Terminal UI	ASCII banner, color-coded findings, live progress spinner
⚙️ Built for Scale	Clean separation of concerns for easy extension into new attack classes
Architecture
SUDARSHAN/
├── crawler/
│   └── crawler.py       # Discovers pages, links, and forms on the target
├── engine/
│   └── engine.py        # Fires payloads at discovered URLs and forms
├── reporter/
│   └── reporter.py       # Renders findings into JSON and HTML reports
├── rules/
│   └── dast_rules.json  # Declarative vulnerability detection rules
├── main.py               # CLI entry point / orchestrator
├── requirements.txt      # Python dependencies
├── LICENSE                # MIT License
└── README.md

Flow: crawler maps the attack surface → engine tests it against rules → reporter compiles the results.

Installation
Clone the repository
bash
git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN
Set up a virtual environment (recommended)
bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
Usage
bash
python3 main.py

You'll be prompted for a target URL:

[?] Enter target URL: https://example.com

SUDARSHAN will then crawl the target, test discovered pages and forms, and write out scan_report.json and scan_report.html.

Sample run
 Enterprise DAST Engine for Modern Web Applications
 Cuts through web vulnerabilities.
 Author: Nilanjan Chowdhury  |  github.com/CalculusGuy/SUDARSHAN

[?] Enter target URL: https://target-app.example

[*] Crawling target...
[+] Found 10 pages, 13 forms

[*] Testing URLs and forms...
[!] Cross-Site Scripting (XSS) detected → payload: <script>alert(1)</script>
[!] SQL Injection detected → payload: ' OR '1'='1

[+] Scan complete! 136 findings.
[+] Reports saved → scan_report.json, scan_report.html
Reports

JSON (scan_report.json) — for pipelines, tooling, and further automation:

json
{
  "target": "https://example.com",
  "scan_date": "2026-08-08T02:23:34.969741",
  "total_findings": 136,
  "findings": [ ]
}

HTML (scan_report.html) — a readable report for humans, with per-finding severity, CWE mapping, and payload detail.

Custom Rules

Detection logic lives entirely in rules/dast_rules.json — no code changes needed to add a new check:

json
{
  "rule_id": "DAST-001",
  "name": "SQL Injection Detection",
  "category": "Injection",
  "severity": "Critical",
  "cwe": "CWE-89",
  "description": "Detects SQL injection vulnerabilities.",
  "attack_vectors": [ ],
  "detection": { }
}
Field Results

Tested against hackthissite.org (a legal, purpose-built pentesting sandbox):

Metric	Result
Pages crawled	10
Forms found	13
Vulnerabilities found	136
Roadmap (Phase 2)
 CLI flags — sudarshan --target https://example.com
 Concurrency — ThreadPoolExecutor for parallel scanning
 Expanded rule set — XXE, CSRF, JWT abuse, and more
 Docker support — containerized deployment
 CI/CD integration — GitHub Actions workflow
 Auth support — login forms, tokens, session cookies
 Proxy support — Burp Suite integration
Legal & Ethical Use

## SUDARSHAN is intended strictly for authorized security testing — your own applications, or targets where you hold explicit written permission (e.g. a bug bounty scope or a sanctioned pentest engagement). Scanning systems without authorization is illegal in most jurisdictions. The author assumes no liability for misuse.

## Contributing

Fork the repository
Create a feature branch (git checkout -b feature/your-feature)
Commit your changes
Open a pull request

Bug reports and rule contributions are especially welcome.

## License

Released under the MIT License.

## Author

Nilanjan Chowdhury

<div align="center">

SUDARSHAN — cuts through web vulnerabilities.
