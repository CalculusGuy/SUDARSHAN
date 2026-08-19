SUDARSHAN — Enterprise DAST Engine
Version: 3.0
Author: Nilanjan Chowdhury
GitHub: github.com/CalculusGuy/SUDARSHAN
License: MIT

WHAT IT IS
Dynamic Application Security Testing (DAST) engine for modern web applications.
Built from scratch in Python with modular architecture, enterprise-grade features, and CI/CD integration.

FEATURES
Feature	Status	Details
Modular Architecture	✅	Crawler, Engine, Reporter
argparse CLI	✅	--target, --threads, --report, --max-pages
Concurrency	✅	ThreadPoolExecutor for parallel scanning
Custom Rules	✅	15 rules (SQLi, XSS, SSRF, XXE, CSRF, JWT, IDOR, etc.)
Multi-Format Reports	✅	JSON + HTML
Logging	✅	File + Console handlers
Unit Tests	✅	8 tests passing (pytest + coverage)
GitHub Actions	✅	CI/CD pipeline
Docker	⏳	Planned
Authentication	⏳	Planned
Proxy Support	⏳	Planned
RESULTS
Metric	Value
Vulnerabilities Found	135+ (on hackthissite.org)
Vulnerabilities Found	24 (on OWASP Juice Shop)
Rules	15
Pages Crawled	10+
Performance	~77 seconds for full scan
Tests Passing	8/8
ARCHITECTURE
text
SUDARSHAN/
├── crawler/
│   └── crawler.py          # Discovers pages and forms
├── engine/
│   └── engine.py           # Tests payloads on URLs and forms
├── reporter/
│   └── reporter.py         # Generates JSON and HTML reports
├── rules/
│   └── dast_rules.json     # 15 vulnerability detection rules
├── tests/
│   └── test_scanner.py     # 8 unit tests
├── logs/
│   └── sudarshan.log       # Application logs
├── .github/workflows/
│   └── ci.yml              # GitHub Actions CI/CD
├── main.py                 # Entry point with CLI
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── README.md               # Documentation
RULES
#	Rule	Severity
1	SQL Injection	Critical
2	Cross-Site Scripting (XSS)	High
3	Server-Side Request Forgery (SSRF)	High
4	Path Traversal	High
5	Command Injection	Critical
6	XXE (XML External Entity)	Critical
7	CSRF (Cross-Site Request Forgery)	High
8	JWT Weakness	High
9	Open Redirect	Medium
10	HTTP Request Smuggling	High
11	IDOR (Insecure Direct Object Reference)	High
12	LDAP Injection	Critical
13	XPATH Injection	High
14	Host Header Injection	Medium
15	NoSQL Injection	Critical
USAGE
bash
python main.py --target https://example.com --threads 20 --report both
TECH STACK
Component	Technology
Language	Python 3.8+
HTTP Client	Requests
HTML Parser	BeautifulSoup4, lxml
Concurrency	ThreadPoolExecutor
Reporting	JSON, HTML
Testing	pytest, pytest-cov, pytest-html
CI/CD	GitHub Actions
Logging	Python logging module
VULNERABILITIES FOUND (Live Targets)
Target	Vulns Found
hackthissite.org	135+
OWASP Juice Shop	24
NEXT PHASES
Phase	Feature
Phase 4	Dockerfile + Containerization
Phase 5	Authentication Support
Phase 6	Proxy Support (Burp Suite)
Phase 7	More Rules (20+)
STATUS
Metric	Value
Version	3.0
Code Coverage	~85%
Tests Passing	8/8
Rules	15
Vulns Found	135+
Platform	Windows, Linux, macOS
Open Source	✅ MIT License
SUDARSHAN — Cuts through web vulnerabilities. 🔥
