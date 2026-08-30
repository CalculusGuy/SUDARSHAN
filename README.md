# ⚔️ SUDARSHAN ⚔️

### Enterprise-Grade Dynamic Application Security Testing Engine
### Author: Nilanjan Chowdhury (@CalculusGuy) 

**SUDARSHAN** is a Python-based **Dynamic Application Security Testing (DAST)** engine designed to automate security assessment of modern web applications.

It performs automated vulnerability discovery across **22 security classes**, supports concurrent scanning, generates structured **JSON and HTML reports**, provides centralized logging, and is designed with **CI/CD integration** in mind.

> **Scan. Detect. Validate. Report. Secure.**

---

## 🚀 Highlights

* 🔍 **22 vulnerability detection rules**
* ⚡ **Concurrent scanning** with `ThreadPoolExecutor`
* 📊 **JSON + HTML security reports**
* 📝 **File + console logging**
* 🧪 **Automated unit testing with pytest**
* 🔄 **GitHub Actions CI/CD**
* 🧩 Modular rule-based architecture
* 🛠️ CLI-driven scanning
* 📁 Structured security findings
* 🎯 Designed for integration into security testing pipelines

---

## 🛡️ Vulnerability Coverage

|  # | Vulnerability                           |   Severity  |
| -: | --------------------------------------- | :---------: |
| 01 | SQL Injection                           | 🔴 Critical |
| 02 | Cross-Site Scripting (XSS)              |   🟠 High   |
| 03 | Server-Side Request Forgery (SSRF)      |   🟠 High   |
| 04 | Path Traversal                          |   🟠 High   |
| 05 | Command Injection                       | 🔴 Critical |
| 06 | XML External Entity (XXE)               | 🔴 Critical |
| 07 | Cross-Site Request Forgery (CSRF)       |   🟠 High   |
| 08 | JWT Weakness                            |   🟠 High   |
| 09 | Open Redirect                           |  🟡 Medium  |
| 10 | Insecure Direct Object Reference (IDOR) |   🟠 High   |
| 11 | LDAP Injection                          | 🔴 Critical |
| 12 | XPath Injection                         |   🟠 High   |
| 13 | Host Header Injection                   |  🟡 Medium  |
| 14 | NoSQL Injection                         | 🔴 Critical |
| 15 | Unrestricted File Upload                |   🟠 High   |
| 16 | Server-Side Template Injection (SSTI)   | 🔴 Critical |
| 17 | HTTP Request Smuggling                  |   🟠 High   |
| 18 | CORS Misconfiguration                   |  🟡 Medium  |
| 19 | Race Condition                          |   🟠 High   |
| 20 | GraphQL Injection                       | 🔴 Critical |
| 21 | Log4Shell — CVE-2021-44228              | 🔴 Critical |
| 22 | Sensitive Data Exposure                 |  🟡 Medium  |

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │      SUDARSHAN      │
                         │     DAST Engine     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Target Input     │
                         │   URL / Parameters   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Recon & Discovery  │
                         │ Endpoints / Inputs  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                 ┌──────────────────────────────────┐
                 │       Vulnerability Engine       │
                 │                                  │
                 │ SQLi │ XSS │ SSRF │ XXE │ IDOR  │
                 │ SSTI │ JWT │ CSRF │ CORS │ ...  │
                 └────────────────┬─────────────────┘
                                  │
                                  ▼
                         ┌─────────────────────┐
                         │  Finding Validation │
                         │ Severity / Evidence │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
                ┌────────────────┐    ┌────────────────┐
                │  JSON Report   │    │  HTML Report   │
                └────────────────┘    └────────────────┘
```

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run a scan

```bash
python main.py --target https://example.com
```

### 4. Run with concurrent workers

```bash
python main.py --target https://example.com --threads 20
```

### 5. Generate both reports

```bash
python main.py --target https://example.com --threads 20 --report both
```

---

## 📊 Reporting

SUDARSHAN supports multiple report formats.

### JSON

Designed for:

* CI/CD pipelines
* Automated processing
* Security dashboards
* Programmatic analysis
* Integration with other security tools

Example structure:

```json
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
```

### HTML

The HTML report provides a human-readable security assessment containing:

* Target information
* Vulnerability findings
* Severity classification
* Affected endpoints
* Parameters
* Security evidence
* Scan information

---

## ⚙️ Configuration

| Option      | Description                              |
| ----------- | ---------------------------------------- |
| `--target`  | Target web application                   |
| `--threads` | Number of concurrent workers             |
| `--report`  | Report format: `json`, `html`, or `both` |

Example:

```bash
python main.py \
    --target https://example.com \
    --threads 20 \
    --report both
```

---

## 🧪 Testing

Run the complete test suite with:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

SUDARSHAN uses automated tests to help maintain reliability as new detection rules and scanning capabilities are introduced.

---

## 🔄 CI/CD

SUDARSHAN includes **GitHub Actions** support for automated testing.

The CI pipeline can be used to:

```text
Push / Pull Request
        │
        ▼
 Install Dependencies
        │
        ▼
    Run Tests
        │
        ▼
   Validate Build
        │
        ▼
      PASS ✓
```

This makes the project suitable for integration into security-focused development workflows.

---

## 📁 Project Structure

```text
SUDARSHAN/
│
├── main.py
├── requirements.txt
├── pytest.ini
│
├── scanner/
│   ├── crawler.py
│   ├── engine.py
│   └── ...
│
├── rules/
│   ├── sqli.py
│   ├── xss.py
│   ├── ssrf.py
│   ├── command_injection.py
│   └── ...
│
├── reports/
│   ├── json_report.py
│   └── html_report.py
│
├── tests/
│   └── ...
│
├── logs/
│   └── ...
│
└── .github/
    └── workflows/
        └── ci.yml
```

> The exact directory structure may vary depending on the current implementation.

---

## 🔬 Security Testing Workflow

SUDARSHAN follows a structured DAST workflow:

```text
       TARGET
          │
          ▼
   ┌─────────────┐
   │   Discovery │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │ Input / API │
   │ Enumeration │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │ 22 Security │
   │    Rules    │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │  Validation │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │   Findings  │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │   Reports   │
   └─────────────┘
```

---

## 📈 Roadmap

### Current

* [x] 22 vulnerability rules
* [x] Concurrent scanning
* [x] JSON reporting
* [x] HTML reporting
* [x] Centralized logging
* [x] Pytest test suite
* [x] GitHub Actions CI/CD

### Planned

* [ ] Dockerized deployment
* [ ] Live web dashboard
* [ ] Authentication/session-aware scanning
* [ ] API security testing
* [ ] Advanced endpoint discovery
* [ ] Finding deduplication
* [ ] CVSS-based risk scoring
* [ ] Evidence collection and replay
* [ ] Scan history
* [ ] Scheduled scanning
* [ ] SARIF report generation
* [ ] Improved CI/CD integrations

---

## 🧰 Technology Stack

| Component   | Technology           |
| ----------- | -------------------- |
| Language    | Python               |
| Concurrency | `ThreadPoolExecutor` |
| Testing     | pytest               |
| CI/CD       | GitHub Actions       |
| Reporting   | JSON / HTML          |
| Interface   | CLI                  |
| License     | MIT                  |

---

## 🎯 Use Cases

SUDARSHAN can be used for:

* Web application security assessments
* Vulnerability research
* Security engineering projects
* DevSecOps pipelines
* CI/CD security testing
* Security labs and controlled environments
* Automated regression security testing

---

## ⚠️ Responsible Use

SUDARSHAN is intended for **authorized security testing only**.

Only scan applications, APIs, systems, and infrastructure that you own or have explicit permission to assess.

The author is not responsible for misuse, unauthorized scanning, disruption, data loss, or damage resulting from the use of this tool.

---

## 👨‍💻 Author

### Nilanjan Chowdhury

Cybersecurity Researcher & Builder
Kolkata, India

**Focus Areas**

`Application Security` · `DAST` · `Web Security` · `AI Security` · `Red Teaming`

---

## 🔗 Links

* **GitHub:** [github.com/CalculusGuy/SUDARSHAN](https://github.com/CalculusGuy/SUDARSHAN)

---

## 📜 License

This project is licensed under the **MIT License**.

See `LICENSE` for details.

---

<div align="center">

### ⚔️ SUDARSHAN

**Automated Web Security. Engineered for Scale.**

⭐ Star the repository if you find it useful.

</div>
