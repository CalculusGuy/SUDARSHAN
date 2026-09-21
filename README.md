⚔️ SUDARSHAN v3.1
Enterprise-Grade Dynamic Application Security Testing Engine
<p align="center"> <b>Scan. Detect. Validate. Prove. Report. Secure.</b> </p><p align="center"> <a href="https://github.com/CalculusGuy/SUDARSHAN"> <img src="https://img.shields.io/badge/GitHub-SUDARSHAN-181717?style=for-the-badge&logo=github" alt="GitHub"> </a> <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/DAST-Web%20Security-DC2626?style=for-the-badge" alt="DAST"> <img src="https://img.shields.io/badge/Rules-22-7C3AED?style=for-the-badge" alt="22 Rules"> <img src="https://img.shields.io/badge/Reports-JSON%20%7C%20HTML-059669?style=for-the-badge" alt="Reports"> <img src="https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge" alt="MIT License"> </p><p align="center"> <i>A Python-based DAST engine for automated web application security assessment, vulnerability discovery, validation, PoC generation, and structured security reporting.</i> </p>
📖 Table of Contents
🐉 What is SUDARSHAN?

🚀 Quick Start — Zero to Scan in 5 Minutes

🧭 Full Guided Walkthrough (Terminal)

🔄 Complete Scan Workflow

🧠 Vulnerability Coverage

🏗️ System Architecture

⚡ Concurrent Scanning

🧪 Finding Validation

🧬 Stacked PoC Generation

📊 Reporting Pipeline

🧰 Full CLI Reference

📁 Understanding the Output

🔬 Test Results

🧪 Testing SUDARSHAN Itself

🔄 CI/CD

📁 Project Structure

🛠️ Technology Stack

🧱 Design Principles

🧭 Roadmap

🔮 Future Architecture

⚠️ Responsible Use

👨‍💻 Author

📜 License

🐉 What is SUDARSHAN?
SUDARSHAN is a modular, Python-based Dynamic Application Security Testing (DAST) engine designed to automate security testing of web applications.

Instead of treating a scanner as a simple collection of payloads, SUDARSHAN is structured as a security assessment pipeline:

text
Target
   │
   ▼
Reconnaissance
   │
   ▼
Endpoint & Input Discovery
   │
   ▼
Attack Surface Mapping
   │
   ▼
Vulnerability Detection
   │
   ▼
Finding Validation
   │
   ▼
Evidence / PoC Generation
   │
   ▼
Risk Classification
   │
   ▼
JSON + HTML Reporting
The project focuses on building the engineering foundations behind an extensible security scanner:

Modular vulnerability rules

Concurrent security testing

Structured findings

Automated validation

Proof-of-concept generation

Evidence collection

Machine-readable reporting

Human-readable reporting

Automated testing

CI/CD integration

🚀 Quick Start — Zero to Scan in 5 Minutes
Prerequisites
Make sure you have these installed:

Requirement	Minimum	Check Command
Python	3.8+	python3 --version
pip	Latest	pip3 --version
git	Any	git --version
If any are missing:

bash
# Debian / Ubuntu / Kali
sudo apt update
sudo apt install python3 python3-pip git -y

# macOS (Homebrew)
brew install python git
Step 1 — Clone the repository
bash
git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN/DAST_Engine
If you cloned before and just want the latest:

bash
cd SUDARSHAN
git pull origin main
cd DAST_Engine
Step 2 — Create an isolated environment (recommended)
bash
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows
You should now see (venv) at the start of your terminal prompt.

Step 3 — Install dependencies
bash
pip install -r requirements.txt
Verify the install:

bash
pip list | grep -i requests
Step 4 — Run your first scan
bash
python main.py --target https://example.com
That's it. You just ran SUDARSHAN.

Step 5 — Run a full scan with reports + PoCs
bash
python main.py \
    --target https://example.com \
    --threads 20 \
    --report both \
    --poc \
    --insecure \
    --max-pages 50
Outputs land in:

text
reports/        → JSON + HTML reports
pocs/           → Generated proof-of-concept scripts
Open the HTML report:

bash
# Linux
xdg-open reports/report.html

# macOS
open reports/report.html

# Windows
start reports/report.html
🧭 Full Guided Walkthrough (Terminal)
This section assumes you have never used SUDARSHAN before. Follow it step by step.

1. Open your terminal
Linux / Kali: Ctrl + Alt + T

macOS: Cmd + Space → type Terminal

Windows: Use WSL or Git Bash (SUDARSHAN targets Unix-like shells)

2. Confirm Python is available
bash
python3 --version
Expected:

text
Python 3.10.x
If you see command not found, install Python first (see Prerequisites).

3. Move to a working directory
bash
mkdir -p ~/tools
cd ~/tools
4. Clone SUDARSHAN
bash
git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN/DAST_Engine
You should now be inside the project folder. Confirm:

bash
ls
You should see files like:

text
main.py   app.py   crawler/   engine/   rules/   reporter/   tests/
5. Set up the virtual environment
bash
python3 -m venv venv
source venv/bin/activate
Your prompt changes to:

text
(venv) user@host:~/tools/SUDARSHAN/DAST_Engine$
To exit later: deactivate

6. Install dependencies
bash
pip install --upgrade pip
pip install -r requirements.txt
If you see permission errors, you forgot to activate the venv. Run source venv/bin/activate again.

7. Verify the CLI works
bash
python main.py --help
You should see the full list of options:

text
usage: main.py [-h] --target TARGET [--threads THREADS] [--report {json,html,both}]
               [--report-dir REPORT_DIR] [--max-pages MAX_PAGES] [--poc]
               [--poc-dir POC_DIR] [--insecure] [--timeout TIMEOUT]
If you see this, SUDARSHAN is ready.

8. Choose a target — legally
Only scan systems you own or have written authorization to test.

Good legal practice targets:

Target	Why
http://localhost:3000	Your local OWASP Juice Shop
http://localhost:8080	Your local Vuln Test App v2.1
https://demo.testfire.net/	IBM's intentionally vulnerable demo
https://hackthissite.org	Legal CTF-style target
Bug bounty program (in-scope only)	Only after reading program rules
Do not scan:

Random websites

Your college / company without written permission

Government sites without authorization

9. Run a basic scan
bash
python main.py --target http://localhost:3000
What happens under the hood:

text
[1] Crawler discovers pages, forms, parameters
[2] Attack surface is built
[3] 22 rules fire concurrently across endpoints
[4] Findings are validated
[5] Console summary is printed
10. Run with concurrency (faster)
bash
python main.py \
    --target http://localhost:3000 \
    --threads 20
Rule of thumb: --threads 10 for shared targets, --threads 20–30 for local labs you own.

11. Increase crawl depth
bash
python main.py \
    --target http://localhost:3000 \
    --max-pages 50
Default is 10. For a full lab app, 50 is reasonable.

12. Generate a JSON report
bash
python main.py \
    --target http://localhost:3000 \
    --report json
Output:

text
reports/report.json
13. Generate an HTML report
bash
python main.py \
    --target http://localhost:3000 \
    --report html
Output:

text
reports/report.html
Open it:

bash
xdg-open reports/report.html      # Linux
open reports/report.html          # macOS
14. Generate both reports
bash
python main.py \
    --target http://localhost:3000 \
    --report both
15. Generate Proof-of-Concept scripts
bash
python main.py \
    --target http://localhost:3000 \
    --poc
Output:

text
pocs/
├── poc_DAST-001.py
├── poc_DAST-002.py
├── poc_DAST-010.py
└── poc_DAST-012.py
Each PoC is runnable:

bash
python pocs/poc_DAST-001.py
The script will try to reproduce the finding and print a confirmation.

16. Full scan — everything enabled
bash
python main.py \
    --target http://localhost:3000 \
    --threads 20 \
    --report both \
    --poc \
    --insecure \
    --max-pages 50 \
    --timeout 15
17. Custom report location
bash
python main.py \
    --target http://localhost:3000 \
    --report both \
    --report-dir ~/assessments/clientname_2026-09-21
18. Custom PoC location
bash
python main.py \
    --target http://localhost:3000 \
    --poc \
    --poc-dir ~/assessments/clientname_pocs
19. Scan a target with a self-signed certificate
bash
python main.py \
    --target https://internal-lab.local \
    --insecure
--insecure disables TLS verification. Only use against systems you own.

20. Complete end-to-end example
bash
# 1. Activate environment
cd ~/tools/SUDARSHAN/DAST_Engine
source venv/bin/activate

# 2. Run full scan
python main.py \
    --target https://demo.testfire.net/ \
    --threads 15 \
    --report both \
    --poc \
    --insecure \
    --max-pages 20

# 3. Review outputs
ls reports/
ls pocs/

# 4. Open HTML report
xdg-open reports/report.html

# 5. Run a generated PoC
python pocs/poc_DAST-001.py
That's the full loop: scan → report → PoC → validate.

21. Deactivate when done
bash
deactivate
22. Troubleshooting
Problem	Cause	Fix
command not found: python3	Python not installed	Install Python 3.8+
No module named requests	venv not active	source venv/bin/activate then pip install -r requirements.txt
SSL: CERTIFICATE_VERIFY_FAILED	Self-signed cert	Add --insecure (lab only)
Scan finishes instantly, 0 findings	Target unreachable or no inputs	Check target URL, increase --max-pages
Permission denied on main.py	File not executable	python main.py ... (no ./)
Timeout errors	Slow target	Increase --timeout 20
Too many requests / rate limit	Threads too high	Reduce --threads to 5
🔄 Complete Scan Workflow

























The 6 stages, in plain English
Stage	What Happens	Output
1. Recon	Crawler walks the app, finds pages/forms/params	Attack surface map
2. Detection	22 rules fire concurrently against each input	Raw findings
3. Validation	Findings are re-checked to reduce false positives	Confirmed findings
4. Evidence	Request/response pairs captured	Evidence records
5. PoC	Runnable scripts generated per vuln class	pocs/*.py
6. Reporting	JSON + HTML reports written	reports/*
🧠 Vulnerability Coverage
SUDARSHAN currently implements 22 vulnerability/security detection classes.

#	Vulnerability	Severity
01	SQL Injection	🔴 Critical
02	Cross-Site Scripting (XSS)	🟠 High
03	Server-Side Request Forgery (SSRF)	🟠 High
04	Path Traversal	🟠 High
05	Command Injection	🔴 Critical
06	XML External Entity (XXE)	🔴 Critical
07	Cross-Site Request Forgery (CSRF)	🟠 High
08	JWT Weakness	🟠 High
09	Open Redirect	🟡 Medium
10	Insecure Direct Object Reference (IDOR)	🟠 High
11	LDAP Injection	🔴 Critical
12	XPath Injection	🟠 High
13	Host Header Injection	🟡 Medium
14	NoSQL Injection	🔴 Critical
15	Unrestricted File Upload	🟠 High
16	Server-Side Template Injection (SSTI)	🔴 Critical
17	HTTP Request Smuggling	🟠 High
18	CORS Misconfiguration	🟡 Medium
19	Race Condition	🟠 High
20	GraphQL Injection	🔴 Critical
21	Log4Shell — CVE-2021-44228	🔴 Critical
22	Sensitive Data Exposure	🟡 Medium
Note: Severity represents the scanner's classification and should not be treated as a final risk rating without application-specific context and manual validation.

🏗️ System Architecture

























⚡ Concurrent Scanning
SUDARSHAN uses Python's ThreadPoolExecutor to execute independent security checks concurrently.














bash
python main.py --target https://example.com --threads 20
Concurrency is configurable from the command line.

🧪 Finding Validation
Detection alone can produce noisy results. SUDARSHAN therefore separates detection from validation.











This architecture provides a foundation for future improvements such as confidence scoring, response-diff analysis, replayable evidence, and finding deduplication.

🧬 Stacked PoC Generation
One of SUDARSHAN's distinctive features is stacked PoC generation. Instead of generating an isolated script for every single request, findings are grouped by vulnerability type.

text
pocs/
├── poc_DAST-001.py
├── poc_DAST-002.py
├── poc_DAST-010.py
└── poc_DAST-012.py












A generated PoC can:

Iterate through related findings

Test each finding

Track successful confirmations

Produce a summary

Execute checks concurrently where appropriate

This creates a bridge between:

text
Scanner Output → Security Finding → Reproducible Validation
📊 Reporting Pipeline











JSON
Designed for CI/CD, automation, dashboards, data processing, and tool integration.

json
{
  "target": "https://example.com",
  "findings": [
    {
      "vulnerability": "Cross-Site Scripting",
      "severity": "High",
      "endpoint": "/search",
      "parameter": "q"
    }
  ]
}
HTML
Designed for human review. Includes target, vulnerability type, severity, endpoint, parameter, evidence, scan information, and finding details.

🧰 Full CLI Reference
Option	Description	Default
--target, -t	Target URL	Required
--threads, -th	Concurrent workers	10
--report, -r	json, html, or both	—
--report-dir	Report output directory	reports
--max-pages, -m	Maximum pages to crawl	10
--poc, -p	Generate PoCs	Disabled
--poc-dir	PoC output directory	pocs
--insecure, -k	Disable TLS verification	Disabled
--timeout	Request timeout (seconds)	10
--help, -h	Show help	—
Recipes
Basic:

bash
python main.py --target https://example.com
Concurrent:

bash
python main.py --target https://example.com --threads 20
With PoCs:

bash
python main.py --target https://example.com --poc
Both reports:

bash
python main.py --target https://example.com --report both
Full:

bash
python main.py \
    --target https://example.com \
    --threads 20 \
    --report both \
    --poc \
    --insecure \
    --max-pages 50
📁 Understanding the Output
After a scan, your project folder looks like this:

text
SUDARSHAN/DAST_Engine/
│
├── reports/
│   ├── report.json          ← machine-readable findings
│   └── report.html          ← human-readable report
│
├── pocs/
│   ├── poc_DAST-001.py      ← runnable PoC
│   ├── poc_DAST-002.py
│   └── ...
│
└── logs/
    └── scan_2026-09-21.log  ← full scan log
Reading a finding
Each finding contains:

text
ID            → DAST-001
Vulnerability → SQL Injection
Severity      → Critical
Endpoint      → /login
Parameter     → username
Evidence      → request + response snippet
PoC           → pocs/poc_DAST-001.py
🔬 Test Results
SUDARSHAN has been exercised against intentionally vulnerable and security-testing targets.

Target	Reported Findings	PoC Generation
demo.testfire.net	334	✅
hackthissite.org	136+	✅
bash
python main.py \
    --target https://demo.testfire.net/ \
    --poc \
    --insecure \
    --threads 15 \
    --max-pages 20
Example output:

text
[+] Found 20 pages, 22 forms
[INFO] Loaded 22 rules
[+] Scan complete! Found 334 vulnerabilities.
[+] PoC scripts generated

  - IDOR
  - XPath Injection
  - NoSQL Injection
  - Sensitive Data Exposure
Important: Scanner-reported findings should be manually validated before being treated as confirmed vulnerabilities. Automated scanners can produce false positives depending on application behavior.

🧪 Testing SUDARSHAN Itself
bash
pytest
Verbose mode:

bash
pytest -v









🔄 CI/CD
SUDARSHAN includes GitHub Actions integration.













Example workflow:

yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
📁 Project Structure
text
SUDARSHAN/
│
├── main.py
├── app.py
├── index.html
│
├── requirements.txt
├── LICENSE
├── README.md
├── Procfile
├── render.yaml
│
├── crawler/
│   └── crawler.py
│
├── engine/
│   └── engine.py
│
├── rules/
│   └── dast_rules.json
│
├── reporter/
│   ├── reporter.py
│   └── poc_generator.py
│
├── tests/
│   └── test_scanner.py
│
├── reports/
│
└── pocs/
Architecture by responsibility
text
┌────────────────────────────────────────────┐
│                  SUDARSHAN                 │
├────────────────────────────────────────────┤
│                                            │
│  Interface                                │
│  ├── CLI                                  │
│  └── API                                  │
│                                            │
│  Discovery                                │
│  └── Crawler                              │
│                                            │
│  Detection                                │
│  ├── Rule Engine                          │
│  └── Security Rules                       │
│                                            │
│  Validation                               │
│  └── Finding Validation                   │
│                                            │
│  Evidence                                 │
│  └── PoC Generator                        │
│                                            │
│  Reporting                                │
│  ├── JSON                                 │
│  └── HTML                                 │
│                                            │
│  Quality                                  │
│  ├── pytest                               │
│  └── GitHub Actions                       │
│                                            │
└────────────────────────────────────────────┘
🛠️ Technology Stack
Layer	Technology
Language	Python
HTTP / Web Testing	Python HTTP tooling
Concurrency	ThreadPoolExecutor
Testing	pytest
CI/CD	GitHub Actions
Reporting	JSON + HTML
Interface	CLI + API wrapper
Deployment	Render configuration
License	MIT
🧱 Design Principles
1. Modular
Security rules are isolated so new detection capabilities can be added without rewriting the scanner.

2. Extensible
The architecture allows future components such as API testing, authentication, session handling, GraphQL, WebSockets, CVSS, SARIF, evidence replay, and scan history.

3. Concurrent
Independent security checks can execute in parallel to reduce scan time.

4. Structured
Findings are represented as structured security data rather than plain console output.

5. Automation-Friendly
JSON output and CLI execution make the scanner suitable for security automation and CI/CD workflows.

6. Validation-Oriented
The long-term direction is to move beyond "Potential vulnerability detected" toward "Vulnerability detected → Evidence collected → PoC generated → Finding tracked → Remediation verified".

🧭 Roadmap
Phase 1 — Core DAST
☑ 22 vulnerability classes
☑ Modular rule engine
☑ Web crawling
☑ Concurrent scanning
☑ Structured findings
☑ JSON reporting
☑ HTML reporting
☑ PoC generation
☑ Centralized logging
☑ Automated testing
☑ GitHub Actions
Phase 2 — Advanced Application Security
□ Authentication-aware scanning
□ Session management
□ Cookie security analysis
□ API discovery
□ REST API testing
□ GraphQL security testing
□ Advanced endpoint discovery
□ Finding deduplication
□ Request/response comparison
Phase 3 — Evidence & Validation
□ Evidence vault
□ Replayable requests
□ Finding lifecycle
□ Confidence scoring
□ CVSS-based risk scoring
□ Remediation tracking
□ Automated re-testing
Phase 4 — DevSecOps
□ SARIF output
□ GitHub Security integration
□ Docker deployment
□ Scheduled scans
□ Scan history
□ Security gates
□ Pipeline failure thresholds
🔮 Future Architecture


















The long-term direction:

text
Discover → Attack → Detect → Prove → Track → Remediate → Retest → Close
⚠️ Responsible Use
SUDARSHAN is a security testing tool.

Only use it against systems you own or systems for which you have explicit authorization to perform security testing.

Do not use SUDARSHAN to:

Scan systems without authorization

Disrupt production services

Access unauthorized data

Circumvent security controls

Perform destructive testing without approval

The author is not responsible for misuse, unauthorized testing, service disruption, data loss, or damage resulting from the use of this software.

👨‍💻 Author
Nilanjan Chowdhury
Cybersecurity Researcher & Security Tool Builder

text
Application Security · DAST · Web Security
AI Security · Red Teaming · Security Engineering
Links:

GitHub: https://github.com/CalculusGuy/SUDARSHAN

Live Demo: https://sudarshan-api-z66i.onrender.com/

Portfolio: https://calculusguy.github.io/nilanjanchowdhury.github.io/

📜 License
SUDARSHAN is released under the MIT License.

See LICENSE for details.

<div align="center">
⚔️ SUDARSHAN
Automated Web Security. Engineered for Scale.
Scan. Detect. Validate. Prove. Report. Secure.

⭐ If SUDARSHAN is useful to you, consider starring the repository.

</div>
