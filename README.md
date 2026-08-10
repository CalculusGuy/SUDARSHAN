# SUDARSHAN

### Enterprise DAST Engine for Modern Web Applications

**SUDARSHAN** is a modular Dynamic Application Security Testing (DAST) engine designed to map web application attack surfaces, execute configurable security tests, and generate actionable vulnerability reports.

Named after the **Sudarshan Chakra**, it is built to cut through the attack surface of modern web applications.

> **For authorized security testing only.**

---

## Core Capabilities

* **Modular DAST Architecture** — Independent crawler, testing engine, and reporting layers.
* **Automated Attack Testing** — Tests discovered URLs and forms against configurable payloads.
* **Rule-Based Detection** — Add vulnerability checks through `rules/dast_rules.json`.
* **Multi-Format Reports** — JSON for automation and HTML for human-readable analysis.
* **Terminal Interface** — Hacker-style CLI with live scan progress and severity-based findings.
* **Extensible Design** — Built to support additional vulnerability classes and integrations.

---

## Architecture

```text
SUDARSHAN/
├── crawler/        # Attack-surface discovery
├── engine/         # Payload execution & testing
├── reporter/       # JSON & HTML reporting
├── rules/          # Declarative DAST rules
├── main.py         # CLI orchestrator
└── requirements.txt
```

**Scan Flow**

```text
Target
  ↓
Crawler
  ↓
Attack Surface
  ↓
DAST Engine
  ↓
Rule-Based Detection
  ↓
JSON + HTML Reports
```

---

## Installation

```bash
git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

Enter an authorized target when prompted.

```text
[?] Enter target URL: https://example.com

[*] Crawling target...
[+] Found 10 pages, 13 forms

[*] Testing attack surface...
[!] XSS detected
[!] SQL Injection detected

[+] Scan complete
[+] Reports → scan_report.json | scan_report.html
```

---

## Rule-Based Detection

Security checks are defined in:

```text
rules/dast_rules.json
```

This allows new detection rules to be introduced without modifying the core engine.

Example:

```json
{
  "rule_id": "DAST-001",
  "name": "SQL Injection Detection",
  "severity": "Critical",
  "cwe": "CWE-89"
}
```

---

## Reports

### JSON

Designed for automation, pipelines, and further analysis.

```json
{
  "target": "https://example.com",
  "total_findings": 136,
  "findings": []
}
```

### HTML

Human-readable vulnerability reporting with severity, CWE mapping, payload information, and findings.

---

## Validation

Tested against **HackThisSite**, a purpose-built security testing environment.

| Metric           | Result |
| ---------------- | -----: |
| Pages crawled    |     10 |
| Forms discovered |     13 |
| Findings         |    136 |

---

## Roadmap

* [ ] CLI arguments
* [ ] Concurrent scanning
* [ ] Expanded vulnerability rules
* [ ] Authentication & session support
* [ ] Proxy / Burp Suite integration
* [ ] Docker deployment
* [ ] CI/CD integration

---

## Legal & Ethical Use

SUDARSHAN is intended **strictly for authorized security testing**.

Only scan applications you own or targets explicitly covered by a bug bounty, penetration-testing engagement, lab, or other written authorization.

The author is not responsible for unauthorized or illegal use.

---

## License

MIT License

## Author

**Nilanjan Chowdhury**

Cybersecurity Researcher | Web Application Security | AI Security

**SUDARSHAN — cuts through web vulnerabilities.**
