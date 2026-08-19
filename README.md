# SUDARSHAN

### Enterprise-Oriented Dynamic Application Security Testing Engine

**SUDARSHAN** is a modular **DAST engine written from scratch in Python** for automated discovery and security testing of modern web applications.

It combines crawling, concurrent security testing, custom vulnerability rules, structured reporting, logging, automated testing, and CI/CD integration into a single security-testing workflow.

> **SUDARSHAN — Cuts through web vulnerabilities. 🔥**

---

## 🚀 Why SUDARSHAN?

Modern web applications expose hundreds of endpoints, parameters, forms, APIs, and authentication flows.

Manually testing every attack surface is slow.

SUDARSHAN automates that process:

```text
                    ┌──────────────────┐
                    │   Target Web App │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Crawler      │
                    │                  │
                    │ URLs • Forms     │
                    │ Parameters       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   DAST Engine    │
                    │                  │
                    │ Concurrent Tests │
                    │ Payloads         │
                    │ Detection Rules  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Vulnerability    │
                    │ Detection        │
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    ▼                  ▼
             ┌─────────────┐    ┌─────────────┐
             │ JSON Report │    │ HTML Report │
             └─────────────┘    └─────────────┘
```

---

# ✨ Features

| Capability             | Status | Description                                            |
| ---------------------- | :----: | ------------------------------------------------------ |
| Modular Architecture   |    ✅   | Crawler, scanning engine, rules and reporting          |
| CLI Interface          |    ✅   | Configurable target, threads, reports and crawl limits |
| Concurrent Scanning    |    ✅   | `ThreadPoolExecutor` based parallel testing            |
| Custom Detection Rules |    ✅   | 15 vulnerability classes                               |
| JSON Reporting         |    ✅   | Machine-readable security findings                     |
| HTML Reporting         |    ✅   | Human-readable vulnerability reports                   |
| Structured Logging     |    ✅   | Console and file logging                               |
| Unit Testing           |    ✅   | `pytest` test suite                                    |
| Code Coverage          |    ✅   | ~85% current coverage                                  |
| GitHub Actions         |    ✅   | Automated CI pipeline                                  |
| Docker                 |   🚧   | Planned                                                |
| Authentication         |   🚧   | Planned                                                |
| Proxy Integration      |   🚧   | Planned                                                |

---

# 🔍 Detection Capabilities

SUDARSHAN currently implements **15 security rules** across multiple vulnerability classes.

|  # | Vulnerability               |   Severity  |
| -: | --------------------------- | :---------: |
| 01 | SQL Injection               | 🔴 Critical |
| 02 | Cross-Site Scripting        |   🟠 High   |
| 03 | Server-Side Request Forgery |   🟠 High   |
| 04 | Path Traversal              |   🟠 High   |
| 05 | Command Injection           | 🔴 Critical |
| 06 | XML External Entity (XXE)   | 🔴 Critical |
| 07 | Cross-Site Request Forgery  |   🟠 High   |
| 08 | JWT Weaknesses              |   🟠 High   |
| 09 | Open Redirect               |  🟡 Medium  |
| 10 | HTTP Request Smuggling      |   🟠 High   |
| 11 | IDOR                        |   🟠 High   |
| 12 | LDAP Injection              | 🔴 Critical |
| 13 | XPath Injection             |   🟠 High   |
| 14 | Host Header Injection       |  🟡 Medium  |
| 15 | NoSQL Injection             | 🔴 Critical |

The rule architecture is designed so additional vulnerability classes can be introduced without rewriting the core crawler or reporting pipeline.

---

# 📊 Benchmark Results

SUDARSHAN has been tested against intentionally vulnerable and publicly available targets.

### OWASP Juice Shop

**24 findings identified**

| Metric          |          Result |
| --------------- | --------------: |
| Vulnerabilities |          **24** |
| Rules           |          **15** |
| Crawl Depth     |       10+ pages |
| Full Scan Time  |     ~77 seconds |
| Test Suite      | **8/8 passing** |
| Code Coverage   |        **~85%** |

### Hack This Site

**135+ findings reported during testing**

> Results depend heavily on target configuration, crawl depth, accessible endpoints, network conditions, and rule behavior. Findings should always be manually validated before being treated as confirmed vulnerabilities.

---

# 🧪 Security Testing Workflow

A typical scan follows this pipeline:

```text
Target
  │
  ▼
URL Discovery
  │
  ├── Pages
  ├── Forms
  └── Parameters
  │
  ▼
Concurrent Security Testing
  │
  ├── Injection Tests
  ├── Client-Side Tests
  ├── Server-Side Tests
  └── Configuration Tests
  │
  ▼
Detection Engine
  │
  ▼
Finding Validation
  │
  ▼
Report Generation
  │
  ├── JSON
  └── HTML
```

---

# 🏗️ Architecture

```text
SUDARSHAN/
│
├── crawler/
│   └── crawler.py
│       └── URL and form discovery
│
├── engine/
│   └── engine.py
│       └── Concurrent security testing
│
├── rules/
│   └── dast_rules.json
│       └── Vulnerability detection rules
│
├── reporter/
│   └── reporter.py
│       └── JSON + HTML reporting
│
├── tests/
│   └── test_scanner.py
│       └── Automated test suite
│
├── logs/
│   └── sudarshan.log
│       └── Runtime logs
│
├── .github/
│   └── workflows/
│       └── ci.yml
│           └── CI pipeline
│
├── main.py
│   └── CLI entry point
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# ⚡ Quick Start

## 1. Clone

```bash
git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run a scan

```bash
python main.py \
    --target https://example.com \
    --threads 20 \
    --report both
```

### Available options

```text
--target       Target URL
--threads      Number of concurrent workers
--report       json | html | both
--max-pages    Maximum number of pages to crawl
```

Example:

```bash
python main.py \
    --target http://localhost:3000 \
    --threads 20 \
    --max-pages 100 \
    --report both
```

---

# 📄 Reporting

SUDARSHAN generates both machine-readable and human-readable reports.

### JSON

Designed for:

* CI/CD pipelines
* Automation
* Security dashboards
* Programmatic processing

### HTML

Designed for:

* Security assessments
* Developer review
* Vulnerability triage
* Evidence presentation

A finding can contain information such as:

```text
Vulnerability
Severity
Target
Endpoint
Parameter
Evidence
Detection Rule
Remediation
```

---

# 🔄 CI/CD Integration

SUDARSHAN includes a **GitHub Actions pipeline** for automated testing.

```text
Developer
    │
    ▼
git push
    │
    ▼
GitHub Actions
    │
    ├── Install dependencies
    ├── Run pytest
    └── Validate project
```

The planned CI/CD evolution is:

```text
Application Build
       │
       ▼
   Deploy Test App
       │
       ▼
   SUDARSHAN DAST
       │
       ▼
 Findings Generated
       │
       ▼
 Severity Evaluation
       │
       ├── PASS
       └── FAIL
```

---

# 🧪 Testing

SUDARSHAN uses `pytest` for automated testing.

Current status:

```text
Tests:       8/8 passing
Coverage:    ~85%
Framework:   pytest
```

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=.
```

---

# 🛠️ Technology Stack

| Component    | Technology           |
| ------------ | -------------------- |
| Language     | Python 3.8+          |
| HTTP Client  | Requests             |
| HTML Parsing | BeautifulSoup4, lxml |
| Concurrency  | ThreadPoolExecutor   |
| CLI          | argparse             |
| Reporting    | JSON, HTML           |
| Testing      | pytest, pytest-cov   |
| CI/CD        | GitHub Actions       |
| Logging      | Python `logging`     |

---

# 🗺️ Roadmap

## v3.x — Reliability & Deployment

* [x] Modular architecture
* [x] Concurrent scanning
* [x] 15 detection rules
* [x] JSON reporting
* [x] HTML reporting
* [x] Logging
* [x] Unit tests
* [x] GitHub Actions
* [ ] Docker containerization

## v4.x — Authenticated DAST

* [ ] Cookie-based authentication
* [ ] Bearer token support
* [ ] Login workflow support
* [ ] Session management
* [ ] Authenticated crawling

## v5.x — Proxy & Advanced Testing

* [ ] HTTP proxy support
* [ ] Burp Suite integration
* [ ] Request/response replay
* [ ] Passive traffic analysis
* [ ] Expanded API testing

## Future

* [ ] 20+ vulnerability rules
* [ ] API/OpenAPI scanning
* [ ] Authentication-aware crawling
* [ ] Finding deduplication
* [ ] Risk scoring
* [ ] SARIF output
* [ ] Security dashboard
* [ ] Distributed scanning

---

# ⚠️ Responsible Use

SUDARSHAN is intended for **authorized security testing only**.

Use it against:

* Applications you own
* Applications you have explicit permission to test
* Intentionally vulnerable environments
* Security labs and CTF platforms where testing is permitted

Do not scan systems without authorization.

The presence of a reported finding does not automatically mean a vulnerability is confirmed. Security findings should be manually validated.

---

# 📜 License

Released under the **MIT License**.

---

# 👨‍💻 Author

**Nilanjan Chowdhury**

Cybersecurity student focused on:

* Application Security
* Penetration Testing
* AI Security
* Security Automation
* DAST

---

# 🔥 SUDARSHAN

> **Automate the hunt. Validate the finding. Secure the application.**

**15 Rules • Concurrent Scanning • Automated Reporting • CI/CD Ready**

⭐ If you find the project useful, consider starring the repository.
