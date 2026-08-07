# SUDARSHAN — Enterprise DAST Engine

**Enterprise-grade Dynamic Application Security Testing (DAST) Engine for modern web applications.**

Built with modular architecture, extensible rule sets, and multi-format reporting.

---

## Features

- **Modular Architecture** — Crawler, Engine, Reporter
- **Customizable Rules** — JSON-based rule sets
- **Multi-Format Reports** — JSON + HTML
- **Hacker Terminal UI** — ASCII banner, color-coded output, progress spinner
- **Built for Scale** — Modular design for easy extension

---

## Results

Tested against `https://www.hackthissite.org/`:

- **Pages Crawled:** 10
- **Forms Found:** 13
- **Vulnerabilities Found:** **136**

---

## Architecture
SUDARSHAN/
├── crawler/
│ └── crawler.py # Discovers pages and forms
├── engine/
│ └── engine.py # Tests payloads on URLs and forms
├── reporter/
│ └── reporter.py # Generates JSON and HTML reports
├── rules/
│ └── dast_rules.json # Custom vulnerability detection rules
├── main.py # Entry point
├── requirements.txt # Python dependencies
├── LICENSE # MIT License
└── README.md # This file

text

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN
```
Install Dependencies
Option 1: Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Option 2: System-wide (Not Recommended)
```bash
pip install -r requirements.txt
```
Run SUDARSHAN
```bash
python3 main.py
```
Usage
Run python3 main.py

Enter target URL (e.g., https://www.hackthissite.org/)

Watch the scanner crawl, attack, and report

## Example Output
   
   Enterprise DAST Engine for Modern Web Applications
   Cuts through web vulnerabilities.
   Author: Nilanjan Chowdhury
   GitHub: github.com/CalculusGuy/SUDARSHAN

[?] Enter target URL: https://www.hackthissite.org/

[*] Scanning: https://www.hackthissite.org/
[*] Crawling pages /
[+] Found 10 pages, 13 forms
[*] Testing URLs...
[+] Testing: https://www.hackthissite.org/
[!] Cross-Site Scripting (XSS) Detection found! Payload: <script>alert(1)</script>
...

[+] Scan complete! Found 136 vulnerabilities.
[+] Reports saved to scan_report.json and scan_report.html
Reports
JSON Report (scan_report.json)
json
{
  "target": "https://www.hackthissite.org/",
  "scan_date": "2026-08-08T02:23:34.969741",
  "total_findings": 136,
  "findings": [...]
}
HTML Report (scan_report.html)
Human-readable report with vulnerability details.

Custom Rules
Add or modify rules in rules/dast_rules.json:

json
{
  "rule_id": "DAST-001",
  "name": "SQL Injection Detection",
  "category": "Injection",
  "severity": "Critical",
  "cwe": "CWE-89",
  "description": "Detects SQL injection vulnerabilities.",
  "attack_vectors": [...],
  "detection": {...}
}
Upcoming Features (Phase 2)
CLI Support — sudarshan --target https://example.com

Concurrency — ThreadPoolExecutor for parallel scanning

More Rules — XXE, CSRF, JWT, etc.

Docker Support — Containerized deployment

CI/CD Integration — GitHub Actions workflow

Authentication — Login forms, tokens, cookies

Proxy Support — Burp Suite integration

## License
MIT License — see LICENSE file.

## Author
Nilanjan Chowdhury

GitHub: CalculusGuy

LinkedIn: Nilanjan Chowdhury

Medium: @nilanjan.calculus

## For Contributing
Fork the repository

Create a feature branch

Submit a pull request

SUDARSHAN — Cuts through web vulnerabilities. 
