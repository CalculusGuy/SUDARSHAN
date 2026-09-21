### ⚔️ SUDARSHAN v3.1

Enterprise-Grade Dynamic Application Security Testing Engine

### Author: Nilanjan Chowdhury (@CalculusGuy)
<p align="center">
  <strong>Scan. Detect. Validate. Prove. Report. Secure.</strong>
</p>

<p align="center">
  <a href="https://github.com/CalculusGuy/SUDARSHAN">
    <img src="https://img.shields.io/badge/GitHub-SUDARSHAN-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/DAST-Web%20Security-DC2626?style=for-the-badge" alt="DAST">
  <img src="https://img.shields.io/badge/Rules-22-7C3AED?style=for-the-badge" alt="22 Rules">
  <img src="https://img.shields.io/badge/Reports-JSON%20%7C%20HTML-059669?style=for-the-badge" alt="Reports">
  <img src="https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge" alt="MIT License">
</p>

<p align="center">
  A Python-based DAST engine for automated web application security assessment,
  vulnerability discovery, finding validation, PoC generation, evidence collection,
  and structured security reporting.
</p>

Table of Contents

Overview

Key Features

Workflow

Architecture

Requirements

Installation

Quick Start

Complete Scan Procedure

CLI Reference

Vulnerability Coverage

Finding Validation

PoC Generation

Reporting

Output Structure

Testing

CI/CD

Project Structure

Technology Stack

Guides

Roadmap

Responsible Use

Author

License

Overview

SUDARSHAN is a modular Dynamic Application Security Testing (DAST) engine written in Python.

It is designed to automate the core stages of a web application security assessment:

Reconnaissance

Endpoint and input discovery

Attack-surface mapping

Vulnerability detection

Finding validation

Evidence collection

Proof-of-concept generation

Risk classification

JSON and HTML reporting

SUDARSHAN is built around an evidence-oriented security workflow, rather than treating a scanner as a simple collection of payloads.

Core Pipeline

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
Evidence Collection
  │
  ▼
PoC Generation
  │
  ▼
Risk Classification
  │
  ▼
JSON / HTML Reporting

Key Features

Feature

Description

22 Security Rules

Detection across multiple web vulnerability classes

Web Crawler

Discovers pages, forms, parameters, and inputs

Concurrent Scanning

Uses ThreadPoolExecutor for parallel checks

Validation Pipeline

Separates detection from finding validation

Evidence Collection

Preserves request/response evidence

PoC Generation

Generates runnable validation scripts

JSON Reporting

Machine-readable output for automation

HTML Reporting

Human-readable security reports

CLI

Configurable scans from the terminal

API Wrapper

API-oriented interface around the engine

Automated Tests

pytest test suite

GitHub Actions

CI/CD testing workflow

MIT Licensed

Open-source licensing

Workflow

End-to-End Assessment Flow

flowchart TD
    A[Target Application] --> B[Reconnaissance]
    B --> C[Web Crawler]
    C --> D[Endpoint & Input Discovery]
    D --> E[Attack Surface Map]

    E --> F[Rule Engine]
    F --> G[Concurrent Security Checks]

    G --> H{Potential Finding?}

    H -->|No| I[Continue Scan]
    I --> G

    H -->|Yes| J[Finding Validation]

    J --> K{Validated?}

    K -->|No| L[Discard / Mark Unconfirmed]
    K -->|Yes| M[Evidence Collection]

    M --> N[PoC Generation]
    N --> O[Risk Classification]
    O --> P[JSON Report]
    O --> Q[HTML Report]

    P --> R[Review & Remediation]
    Q --> R

    R --> S[Retest]
    S --> T[Close Finding]

Six Core Stages

Stage

What Happens

Output

1. Recon

Crawler walks the application

Attack surface

2. Detection

Security rules test discovered inputs

Raw findings

3. Validation

Findings are re-checked

Validated findings

4. Evidence

Relevant request/response data is captured

Evidence

5. PoC

Reproducible scripts are generated

pocs/*.py

6. Reporting

Results are exported

JSON + HTML

Security Testing Loop

Discover
   ↓
Attack
   ↓
Detect
   ↓
Validate
   ↓
Prove
   ↓
Report
   ↓
Remediate
   ↓
Retest

Architecture

High-Level Architecture

flowchart LR
    A[CLI / API] --> B[Crawler]
    B --> C[Attack Surface]
    C --> D[Rule Engine]

    D --> E[Security Rules]
    E --> F[Concurrent Execution]

    F --> G[Finding Validation]
    G --> H[Evidence Layer]

    H --> I[PoC Generator]
    H --> J[Finding Model]

    J --> K[JSON Reporter]
    J --> L[HTML Reporter]

    K --> M[Automation / CI]
    L --> N[Human Review]

Component Responsibilities

SUDARSHAN
│
├── Interface
│   ├── CLI
│   └── API
│
├── Discovery
│   └── Crawler
│
├── Detection
│   ├── Rule Engine
│   └── Security Rules
│
├── Validation
│   └── Finding Validation
│
├── Evidence
│   └── PoC Generator
│
├── Reporting
│   ├── JSON
│   └── HTML
│
└── Quality
    ├── pytest
    └── GitHub Actions

Requirements

System Requirements

Requirement

Minimum

Python

3.8+

pip

Latest recommended

Git

Any recent version

Network

Required for remote targets

OS

Linux, macOS, or Windows-compatible Python environment

Verify Requirements

python3 --version
pip3 --version
git --version

Expected Python version:

Python 3.8+

Installation

1. Clone the Repository

git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN/DAST_Engine

2. Create a Virtual Environment

Linux / macOS

python3 -m venv venv
source venv/bin/activate

Windows

python -m venv venv
venv\Scripts\activate

Your shell should now show something similar to:

(venv) user@host:~/SUDARSHAN/DAST_Engine$

3. Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

4. Verify Installation

python main.py --help

If the CLI help is displayed, SUDARSHAN is ready.

Quick Start

Basic Scan

python main.py --target https://example.com

Scan a Local Lab

python main.py --target http://localhost:3000

Scan with Concurrency

python main.py \
    --target http://localhost:3000 \
    --threads 20

Generate JSON Report

python main.py \
    --target http://localhost:3000 \
    --report json

Generate HTML Report

python main.py \
    --target http://localhost:3000 \
    --report html

Generate Both Reports

python main.py \
    --target http://localhost:3000 \
    --report both

Generate PoCs

python main.py \
    --target http://localhost:3000 \
    --poc

Full Scan

python main.py \
    --target http://localhost:3000 \
    --threads 20 \
    --report both \
    --poc \
    --max-pages 50 \
    --timeout 15

Complete Scan Procedure

This is the recommended procedure for running a complete assessment.

Step 1 — Prepare the Environment

cd SUDARSHAN/DAST_Engine
source venv/bin/activate

Verify:

python main.py --help

Step 2 — Select an Authorized Target

Only test applications that you own or have explicit authorization to assess.

Suitable environments include:

Your own local applications

OWASP Juice Shop running locally

Intentionally vulnerable training applications

Authorized bug-bounty targets within scope

Authorized client or organizational systems

Example:

python main.py --target http://localhost:3000

Step 3 — Run Reconnaissance

SUDARSHAN begins by crawling the target and discovering:

Pages
Forms
Parameters
Inputs
Endpoints
Attack Surface

Example:

python main.py \
    --target http://localhost:3000 \
    --max-pages 50

Step 4 — Execute Security Rules

The rule engine applies the configured vulnerability checks.

Attack Surface
      │
      ▼
  Rule Engine
      │
      ├── SQL Injection
      ├── XSS
      ├── SSRF
      ├── Path Traversal
      ├── Command Injection
      ├── XXE
      └── ... 22 classes

Concurrent execution can be enabled with:

--threads 20

Step 5 — Validate Findings

Detected findings are passed through the validation stage.

Detection
    │
    ▼
Potential Finding
    │
    ▼
Validation
    │
    ├── Not validated
    │
    └── Validated
            │
            ▼
        Evidence

This helps distinguish scanner detections from findings that require further verification.

Step 6 — Generate Evidence and PoCs

Run:

python main.py \
    --target http://localhost:3000 \
    --poc

PoCs are written to:

pocs/

Example:

pocs/
├── poc_DAST-001.py
├── poc_DAST-002.py
└── poc_DAST-010.py

Step 7 — Generate Reports

python main.py \
    --target http://localhost:3000 \
    --report both

Outputs:

reports/
├── report.json
└── report.html

Step 8 — Review Results

JSON

Use JSON for:

Automation

CI/CD

Dashboards

Data processing

Tool integration

HTML

Use HTML for:

Human review

Security assessment documentation

Finding analysis

Evidence review

Step 9 — Retest

After remediation, run SUDARSHAN again against the authorized target.

python main.py \
    --target http://localhost:3000 \
    --report both \
    --poc

The intended lifecycle is:

Finding
   ↓
Remediation
   ↓
Retest
   ↓
Validation
   ↓
Close

CLI Reference

Run:

python main.py --help

Option

Description

Default

--target, -t

Target URL

Required

--threads, -th

Concurrent workers

10

--report, -r

json, html, or both

—

--report-dir

Report output directory

reports

--max-pages, -m

Maximum pages to crawl

10

--poc, -p

Generate PoCs

Disabled

--poc-dir

PoC output directory

pocs

--insecure, -k

Disable TLS verification

Disabled

--timeout

Request timeout in seconds

10

--help, -h

Show CLI help

—

CLI Recipes

Basic

python main.py --target https://example.com

Fast / Concurrent

python main.py \
    --target https://example.com \
    --threads 20

Increase Crawl Depth

python main.py \
    --target https://example.com \
    --max-pages 50

JSON

python main.py \
    --target https://example.com \
    --report json

HTML

python main.py \
    --target https://example.com \
    --report html

Both Reports + PoCs

python main.py \
    --target https://example.com \
    --report both \
    --poc

Custom Report Directory

python main.py \
    --target http://localhost:3000 \
    --report both \
    --report-dir ~/assessments/client_2026-09-21

Custom PoC Directory

python main.py \
    --target http://localhost:3000 \
    --poc \
    --poc-dir ~/assessments/client_pocs

Self-Signed Certificate

python main.py \
    --target https://internal-lab.local \
    --insecure

--insecure disables TLS certificate verification. Use it only where you are authorized to do so, such as a controlled lab.

Vulnerability Coverage

SUDARSHAN currently implements 22 vulnerability/security detection classes.

#

Vulnerability

Severity

01

SQL Injection

Critical

02

Cross-Site Scripting (XSS)

High

03

Server-Side Request Forgery (SSRF)

High

04

Path Traversal

High

05

Command Injection

Critical

06

XML External Entity (XXE)

Critical

07

Cross-Site Request Forgery (CSRF)

High

08

JWT Weakness

High

09

Open Redirect

Medium

10

Insecure Direct Object Reference (IDOR)

High

11

LDAP Injection

Critical

12

XPath Injection

High

13

Host Header Injection

Medium

14

NoSQL Injection

Critical

15

Unrestricted File Upload

High

16

Server-Side Template Injection (SSTI)

Critical

17

HTTP Request Smuggling

High

18

CORS Misconfiguration

Medium

19

Race Condition

High

20

GraphQL Injection

Critical

21

Log4Shell — CVE-2021-44228

Critical

22

Sensitive Data Exposure

Medium

Note: Severity is the scanner's classification. It should not be treated as a final risk rating without application-specific context and manual validation.

Concurrent Scanning

SUDARSHAN uses Python's ThreadPoolExecutor to execute independent checks concurrently.

python main.py \
    --target https://example.com \
    --threads 20

Conceptually:

                  Target
                    │
                    ▼
              Attack Surface
                    │
                    ▼
              ┌───────────┐
              │ Rule Pool │
              └─────┬─────┘
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    Rule 01      Rule 02      Rule 03
       │            │            │
       └────────────┼────────────┘
                    ▼
              Finding Results

Concurrency is configurable from the CLI.

Finding Validation

Detection and validation are intentionally separated.

flowchart TD
    A[Input / Endpoint] --> B[Security Rule]
    B --> C{Detection}
    C -->|No signal| D[Continue]
    C -->|Potential issue| E[Validation]

    E --> F{Validated?}
    F -->|No| G[Unconfirmed / Discard]
    F -->|Yes| H[Evidence]
    H --> I[PoC]
    I --> J[Report]

This provides a foundation for:

Response-diff analysis

Confidence scoring

Evidence replay

Finding deduplication

Reproducible validation

PoC Generation

SUDARSHAN supports stacked PoC generation.

Instead of producing only raw scanner output, the engine can generate scripts associated with detected vulnerability classes.

Example:

pocs/
├── poc_DAST-001.py
├── poc_DAST-002.py
├── poc_DAST-010.py
└── poc_DAST-012.py

A generated PoC can:

Iterate through related findings

Re-test detected conditions

Track successful confirmations

Produce a validation summary

Execute checks concurrently where appropriate

Conceptually:

Scanner Output
      ↓
Security Finding
      ↓
Evidence
      ↓
Generated PoC
      ↓
Reproducible Validation

Reporting

JSON Report

Example:

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

JSON is intended for:

CI/CD

Automation

Dashboards

Data processing

Security-tool integration

HTML Report

The HTML report is intended for human review and includes information such as:

Target

Vulnerability type

Severity

Endpoint

Parameter

Evidence

Scan information

Finding details

Output Structure

After a scan:

SUDARSHAN/DAST_Engine/
│
├── reports/
│   ├── report.json
│   └── report.html
│
├── pocs/
│   ├── poc_DAST-001.py
│   ├── poc_DAST-002.py
│   └── ...
│
└── logs/
    └── scan_YYYY-MM-DD.log

Finding Structure

A finding contains information such as:

ID            → DAST-001
Vulnerability → SQL Injection
Severity      → Critical
Endpoint      → /login
Parameter     → username
Evidence      → Request + response data
PoC           → pocs/poc_DAST-001.py

Test Results

SUDARSHAN has been exercised against intentionally vulnerable and security-testing targets.

Target

Reported Findings

PoC Generation

demo.testfire.net

334

✅

hackthissite.org

136+

✅

Example:

python main.py \
    --target https://demo.testfire.net/ \
    --poc \
    --insecure \
    --threads 15 \
    --max-pages 20

Example output:

[+] Found 20 pages, 22 forms
[INFO] Loaded 22 rules
[+] Scan complete! Found 334 vulnerabilities.
[+] PoC scripts generated

Important: Scanner-reported findings should be manually validated before being treated as confirmed vulnerabilities. Automated scanners can produce false positives depending on application behavior.

Testing

Run the test suite:

pytest

Verbose mode:

pytest -v

Testing is intended to verify scanner behavior and protect against regressions as new rules and capabilities are added.

CI/CD

SUDARSHAN includes GitHub Actions integration.

Example:

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

Workflow:

Push / Pull Request
        │
        ▼
 GitHub Actions
        │
        ▼
 Checkout Repository
        │
        ▼
 Setup Python
        │
        ▼
 Install Dependencies
        │
        ▼
      pytest
        │
        ▼
   Test Result

Project Structure

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
└── pocs/

Guides

Guide 1 — First Scan

Install
  ↓
Clone
  ↓
Create venv
  ↓
Install requirements
  ↓
Run --help
  ↓
Choose authorized target
  ↓
Run scan
  ↓
Review findings

Command sequence:

git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN/DAST_Engine

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python main.py --help

python main.py \
    --target http://localhost:3000 \
    --report both \
    --poc

Guide 2 — Local Vulnerable Lab

A recommended workflow is to use an intentionally vulnerable application running locally.

Local Vulnerable App
        │
        ▼
   SUDARSHAN
        │
        ├── Crawl
        ├── Discover
        ├── Detect
        ├── Validate
        └── Report

Example:

python main.py \
    --target http://localhost:3000 \
    --threads 20 \
    --max-pages 50 \
    --report both \
    --poc

Guide 3 — Assessment with Custom Output Directories

mkdir -p ~/assessments/client_2026-09-21

python main.py \
    --target http://localhost:3000 \
    --report both \
    --report-dir ~/assessments/client_2026-09-21 \
    --poc \
    --poc-dir ~/assessments/client_2026-09-21/pocs

This keeps reports and PoCs separated from the source tree.

Guide 4 — Full Assessment Loop

┌─────────────────────┐
│  Define Scope       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Recon / Discovery  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Automated Testing  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Validate Findings  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Collect Evidence   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Generate PoCs      │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Generate Reports   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Remediate          │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Retest             │
└──────────┬──────────┘
           ↓
      Close Finding

Technology Stack

Layer

Technology

Language

Python

HTTP / Web Testing

Python HTTP tooling

Concurrency

ThreadPoolExecutor

Testing

pytest

CI/CD

GitHub Actions

Reporting

JSON + HTML

Interface

CLI + API wrapper

Deployment

Render configuration

License

MIT

Design Principles

1. Modular

Security rules are isolated so new detection capabilities can be added without rewriting the scanner.

2. Extensible

The architecture allows future components such as authentication, session handling, API testing, GraphQL, WebSockets, CVSS, SARIF, evidence replay, and scan history.

3. Concurrent

Independent security checks can execute in parallel to reduce scan time.

4. Structured

Findings are represented as structured security data rather than plain console output.

5. Automation-Friendly

JSON output and CLI execution make the scanner suitable for security automation and CI/CD workflows.

6. Validation-Oriented

The long-term direction is to move beyond:

"Potential vulnerability detected"

toward:

Vulnerability Detected
        ↓
Evidence Collected
        ↓
PoC Generated
        ↓
Finding Tracked
        ↓
Remediation Verified
        ↓
Retest
        ↓
Closed

Roadmap

Phase 1 — Core DAST

22 vulnerability classes

Modular rule engine

Web crawling

Concurrent scanning

Structured findings

JSON reporting

HTML reporting

PoC generation

Centralized logging

Automated testing

GitHub Actions

Phase 2 — Advanced Application Security

Authentication-aware scanning

Session management

Cookie security analysis

API discovery

REST API testing

GraphQL security testing

Advanced endpoint discovery

Finding deduplication

Request/response comparison

Phase 3 — Evidence & Validation

Evidence vault

Replayable requests

Finding lifecycle

Confidence scoring

CVSS-based risk scoring

Remediation tracking

Automated re-testing

Phase 4 — DevSecOps

SARIF output

GitHub Security integration

Docker deployment

Scheduled scans

Scan history

Security gates

Pipeline failure thresholds

Future Architecture

The long-term direction of SUDARSHAN is:

Discover
   ↓
Attack
   ↓
Detect
   ↓
Prove
   ↓
Track
   ↓
Remediate
   ↓
Retest
   ↓
Close

Responsible Use

SUDARSHAN is a security testing tool.

Only use it against systems you own or systems for which you have explicit authorization to perform security testing.

Do not use SUDARSHAN to:

Scan systems without authorization

Disrupt production services

Access unauthorized data

Circumvent security controls

Perform destructive testing without approval

The author is not responsible for misuse, unauthorized testing, service disruption, data loss, or damage resulting from the use of this software.

Author

Nilanjan Chowdhury

Cybersecurity Researcher & Security Tool Builder

Application Security · DAST · Web Security
AI Security · Red Teaming · Security Engineering

Links

GitHub: https://github.com/CalculusGuy/SUDARSHAN

Live Demo: https://sudarshan-api-z66i.onrender.com/

Portfolio: https://calculusguy.github.io/nilanjanchowdhury.github.io/

License

SUDARSHAN is released under the MIT License.

See LICENSE for details.

<div align="center">

⚔️ SUDARSHAN

Automated Web Security. Engineered for Scale.

Scan. Detect. Validate. Prove. Report. Secure.

⭐ Star the repository if you find SUDARSHAN useful.

</div>
