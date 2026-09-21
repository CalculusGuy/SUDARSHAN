⚔️ SUDARSHAN v3.1

Enterprise-Grade Dynamic Application Security Testing Engine

<p align="center">
  <b>Scan. Detect. Validate. Prove. Report. Secure.</b>
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
  vulnerability discovery, validation, PoC generation, evidence collection,
  and structured security reporting.
</p>

Overview

SUDARSHAN is a modular Dynamic Application Security Testing (DAST) engine designed to automate security testing of web applications.

Rather than treating a scanner as a collection of payloads, SUDARSHAN follows an assessment pipeline:

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

Core Capabilities

Modular vulnerability detection rules

Concurrent security testing

Automated finding validation

Evidence collection

Runnable proof-of-concept generation

JSON and HTML reporting

CLI and API interfaces

Automated testing with pytest

GitHub Actions CI/CD integration

Quick Start

Requirements

Requirement

Version

Python

3.8+

pip

Latest

Git

Any

1. Clone

git clone https://github.com/CalculusGuy/SUDARSHAN.git
cd SUDARSHAN/DAST_Engine

2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate

# Windows
# venv\Scripts\activate

3. Install dependencies

pip install --upgrade pip
pip install -r requirements.txt

4. Verify the CLI

python main.py --help

5. Run a scan

python main.py --target https://example.com

Full scan

python main.py \
    --target https://example.com \
    --threads 20 \
    --report both \
    --poc \
    --insecure \
    --max-pages 50

Generated files:

reports/
├── report.json
└── report.html

pocs/
├── poc_DAST-001.py
├── poc_DAST-002.py
└── ...

Scan Workflow

SUDARSHAN follows a six-stage security testing workflow:

Stage

Description

Output

1. Recon

Crawl pages, forms, and parameters

Attack surface

2. Detection

Execute security rules concurrently

Raw findings

3. Validation

Re-check detected issues

Confirmed findings

4. Evidence

Capture relevant request/response data

Evidence records

5. PoC

Generate reproducible scripts

pocs/*.py

6. Reporting

Export structured results

JSON + HTML

Discover → Attack → Detect → Validate → Prove → Report

Vulnerability Coverage

SUDARSHAN currently implements 22 vulnerability/security detection classes:

#

Vulnerability

Scanner Severity

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

Note: Severity represents the scanner's classification and should not be treated as a final risk rating without application-specific context and manual validation.

Architecture

                         ┌─────────────────────┐
                         │      SUDARSHAN      │
                         └──────────┬──────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
             Interface          Discovery         Detection
             CLI / API           Crawler          Rule Engine
                                                     │
                                                     ▼
                                                22 Rules
                                                     │
                  ┌──────────────────────────────────┘
                  │
                  ▼
              Validation
                  │
                  ▼
             Evidence / PoC
                  │
                  ▼
              Reporting
             ┌────┴────┐
             ▼         ▼
           JSON       HTML

Design

SUDARSHAN separates responsibilities into modular components:

Interface
├── CLI
└── API

Discovery
└── Crawler

Detection
├── Rule Engine
└── Security Rules

Validation
└── Finding Validation

Evidence
└── PoC Generator

Reporting
├── JSON
└── HTML

Quality
├── pytest
└── GitHub Actions

Concurrent Scanning

SUDARSHAN uses Python's ThreadPoolExecutor to execute independent security checks concurrently.

python main.py --target https://example.com --threads 20

Concurrency is configurable through the CLI.

Finding Validation

Detection and validation are separate stages.

Potential Finding
      │
      ▼
Validation
      │
      ├── False Positive
      │
      └── Valid Finding
              │
              ▼
          Evidence
              │
              ▼
             PoC

This architecture provides a foundation for response-diff analysis, replayable evidence, finding deduplication, and confidence scoring.

PoC Generation

SUDARSHAN can generate runnable proof-of-concept scripts for detected findings.

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

The intended flow is:

Scanner Output
      ↓
Security Finding
      ↓
Reproducible Validation

Reporting

JSON

Designed for automation, CI/CD pipelines, dashboards, and tool integration.

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

Designed for human review and includes target information, vulnerability type, severity, endpoint, parameter, evidence, scan information, and finding details.

CLI Reference

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

Show help

—

Examples

Basic

python main.py --target https://example.com

Concurrent

python main.py --target https://example.com --threads 20

Generate PoCs

python main.py --target https://example.com --poc

Generate both reports

python main.py --target https://example.com --report both

Full

python main.py \
    --target https://example.com \
    --threads 20 \
    --report both \
    --poc \
    --insecure \
    --max-pages 50

Output Structure

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

Example console output:

[+] Found 20 pages, 22 forms
[INFO] Loaded 22 rules
[+] Scan complete! Found 334 vulnerabilities.
[+] PoC scripts generated

Important: Scanner-reported findings should be manually validated before being treated as confirmed vulnerabilities. Automated scanners can produce false positives depending on application behavior.

Testing

Run the test suite with:

pytest

Verbose mode:

pytest -v

CI/CD

SUDARSHAN includes GitHub Actions integration.

Example workflow:

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

Project Structure

SUDARSHAN/
│
├── main.py
├── app.py
├── index.html
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

Modular

Security rules are isolated so new detection capabilities can be added without rewriting the scanner.

Extensible

The architecture allows future components such as authentication, session handling, API testing, GraphQL, WebSockets, CVSS, SARIF, evidence replay, and scan history.

Concurrent

Independent security checks can execute in parallel to reduce scan time.

Structured

Findings are represented as structured security data rather than plain console output.

Automation-Friendly

JSON output and CLI execution make SUDARSHAN suitable for security automation and CI/CD workflows.

Validation-Oriented

The long-term direction is:

Potential Finding
      ↓
Evidence Collected
      ↓
PoC Generated
      ↓
Finding Tracked
      ↓
Remediation Verified

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

Future Direction

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
