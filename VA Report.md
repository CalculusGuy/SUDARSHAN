# SUDARSHAN — OWASP Juice Shop DAST Assessment

**Dynamic Application Security Testing Report**

| Field                 | Details                                        |
| --------------------- | ---------------------------------------------- |
| **Assessment Target** | OWASP Juice Shop                               |
| **Target URL**        | `http://localhost:30**`                        |
| **Assessment Type**   | Black-box Dynamic Application Security Testing |
| **Scanner**           | SUDARSHAN v2                                   |
| **Assessment Date**   | August 13, 2026                                |
| **Author**            | Nilanjan Chowdhury                             |
| **Environment**       | Local Docker                                   |
| **Authorization**     | Authorized local security testing              |

---

## 1. Executive Summary

A Dynamic Application Security Testing (DAST) assessment was performed against a locally deployed instance of **OWASP Juice Shop** using **SUDARSHAN v2**, an automated web application security testing engine developed by Nilanjan Chowdhury.

The assessment identified **24 vulnerability findings** across two vulnerability classes:

| Severity     | Vulnerability                 | Findings |
| ------------ | ----------------------------- | -------: |
| **Critical** | Command Injection (CWE-78)    |        8 |
| **High**     | Cross-Site Scripting (CWE-79) |       16 |
|              | **Total**                     |   **24** |

The scan demonstrates SUDARSHAN's ability to automatically discover potentially exploitable application behaviors through HTTP-based interaction and payload injection.

Because OWASP Juice Shop is intentionally vulnerable, these results should be interpreted as **validation of scanner detection capabilities rather than evidence of a production compromise**.

### Key Takeaways

* 24 findings were automatically identified.
* Command Injection represented the highest-risk vulnerability class.
* XSS represented the largest number of findings.
* Findings were generated through automated payload injection.
* Machine-readable and human-readable scan reports were generated.
* The assessment was performed entirely within an authorized local Docker environment.

---

# 2. Assessment Scope

### Target

`http://localhost:3000`

### Application

**OWASP Juice Shop**

### Testing Methodology

SUDARSHAN performed black-box DAST by interacting with the target application over HTTP and injecting security test payloads into identified input locations.

The assessment focused on identifying application behavior consistent with:

* Cross-Site Scripting
* Command Injection
* Unsafe handling of user-controlled input
* Potential server-side command execution
* Improper output handling

No source code was required by the scanner during the assessment.

---

# 3. Findings Overview

| ID      | Vulnerability        | CWE    | Severity |  Count |
| ------- | -------------------- | ------ | -------- | -----: |
| SUD-XSS | Cross-Site Scripting | CWE-79 | High     |     16 |
| SUD-CMD | Command Injection    | CWE-78 | Critical |      8 |
|         | **Total**            |        |          | **24** |

### Severity Distribution

**Critical:** 8 findings
**High:** 16 findings

The assessment produced no Medium, Low, or Informational findings within the vulnerability classes currently implemented and triggered during this scan.

---

# 4. Detailed Findings

## 4.1 Cross-Site Scripting

**Severity:** High
**CWE:** CWE-79
**Category:** Improper Neutralization of Input During Web Page Generation

### Description

The application processes user-controlled input in a manner that can result in executable content being interpreted by the browser.

SUDARSHAN identified multiple locations where XSS test payloads produced behavior consistent with insufficient input/output handling.

### Affected Input Locations

* `q`
* `comment`

### Proof of Concept

```html
<script>alert(1)</script>
```

A successful execution of the payload demonstrates that attacker-controlled content can reach a browser execution context without adequate protection.

### Potential Impact

Depending on the application's execution context, successful XSS exploitation may allow an attacker to:

* Execute arbitrary JavaScript in a victim's browser
* Perform actions using the victim's authenticated session
* Access data exposed to client-side JavaScript
* Modify rendered application content
* Conduct phishing or UI redressing attacks
* Potentially compromise application workflows

### Remediation

1. Implement context-aware output encoding.
2. Treat all externally supplied data as untrusted.
3. Apply appropriate HTML, JavaScript, CSS, and URL encoding depending on the output context.
4. Avoid unsafe DOM APIs such as `innerHTML` when processing untrusted data.
5. Use a well-maintained sanitization library where HTML input is intentionally permitted.
6. Deploy a restrictive **Content Security Policy (CSP)** as defense in depth.
7. Validate security controls through automated regression testing.

---

## 4.2 Command Injection

**Severity:** Critical
**CWE:** CWE-78
**Category:** Improper Neutralization of Special Elements used in an OS Command

### Description

The application appears to incorporate attacker-controlled input into an operating-system command execution context without sufficient separation between data and commands.

SUDARSHAN detected behavior consistent with command injection across multiple tested inputs.

### Affected Input Locations

* `host`
* `ping`

### Proof of Concept

```bash
127.0.0.1; whoami
```

The payload attempts to terminate the intended command and introduce an additional operating-system command.

### Potential Impact

Successful command injection can potentially allow an attacker to:

* Execute arbitrary commands on the application server
* Read sensitive files
* Access environment variables and secrets
* Modify application data
* Establish persistence
* Pivot toward internal services
* Potentially achieve full server compromise

The actual impact depends on the privileges of the application process and the security controls surrounding the deployment.

### Remediation

#### Preferred Approach

Avoid invoking a shell whenever possible.

For example, instead of constructing a shell command dynamically:

```python
subprocess.run(command, shell=True)
```

use argument-based execution:

```python
subprocess.run(
    ["ping", "-c", "1", host],
    check=True
)
```

Additional controls should include:

* Strict allowlist-based input validation
* Avoiding `shell=True`
* Separating command arguments from user-controlled data
* Restricting application process privileges
* Applying container and OS-level isolation
* Implementing network egress restrictions
* Logging suspicious command execution attempts

Input validation should be treated as **defense in depth**, not as a replacement for safe command invocation.

---

# 5. Risk Assessment

The findings demonstrate two different classes of application security weakness.

### Command Injection — Critical

Command injection represents the most significant risk because successful exploitation may cross the application boundary and result in operating-system-level code execution.

**Risk:** Potential server compromise

### Cross-Site Scripting — High

XSS can compromise users interacting with the vulnerable application and may enable unauthorized actions or manipulation of application content.

**Risk:** Potential client-side compromise and session abuse

---

# 6. Remediation Priorities

| Priority          | Action                                                      | Objective                      |
| ----------------- | ----------------------------------------------------------- | ------------------------------ |
| **P0 — Critical** | Eliminate shell-based command construction                  | Prevent OS command execution   |
| **P0 — Critical** | Replace `shell=True` patterns with argument-based execution | Separate data from commands    |
| **P1 — High**     | Implement context-aware output encoding                     | Prevent XSS                    |
| **P1 — High**     | Review DOM-based data flows                                 | Prevent client-side injection  |
| **P1 — High**     | Deploy restrictive CSP                                      | Reduce XSS impact              |
| **P2 — Medium**   | Add security regression tests                               | Prevent recurrence             |
| **P2 — Medium**   | Integrate SUDARSHAN into CI/CD                              | Detect vulnerabilities earlier |

---

# 7. Scanner Validation

This assessment was performed to validate the automated detection capabilities of SUDARSHAN.

The scan demonstrated the engine's ability to:

* Discover application input locations
* Inject security-oriented test payloads
* Detect potentially vulnerable application behavior
* Classify findings by vulnerability type
* Assign severity levels
* Associate findings with CWE classifications
* Generate machine-readable scan output
* Generate human-readable assessment reports

These capabilities form the foundation for expanding SUDARSHAN into a broader automated DAST platform.

---

# 8. Limitations

This assessment has several limitations:

* Testing was performed against an intentionally vulnerable application.
* The target was running in a local Docker environment.
* Findings represent scanner detections and should be manually validated before being treated as confirmed production vulnerabilities.
* The assessment did not evaluate authentication/authorization weaknesses unless covered by the implemented scanner rules.
* Coverage is dependent on the vulnerability detection modules currently implemented in SUDARSHAN.
* No production infrastructure was tested.

---

# 9. Conclusion

SUDARSHAN successfully identified **24 security findings** during the OWASP Juice Shop assessment, including:

* **8 Critical Command Injection findings**
* **16 High Cross-Site Scripting findings**

The assessment demonstrates that SUDARSHAN can automatically interact with a web application, inject security test payloads, identify suspicious application behavior, classify vulnerabilities, and produce structured security assessment output.

This assessment represents a validation milestone for the SUDARSHAN DAST engine and provides a foundation for expanding its detection coverage, reducing false positives, improving evidence collection, and integrating automated security testing into development and CI/CD workflows.

---

## 10. Assessment Artifacts

The following artifacts were generated during the assessment:

```text
scan_report.json
scan_report.html
```

### Machine-Readable Output

`scan_report.json` contains the raw scanner results and can be consumed by automation, dashboards, or CI/CD security pipelines.

### Human-Readable Output

`scan_report.html` provides a browser-friendly representation of the assessment findings.

---

## 11. Project Context

**SUDARSHAN** is an open-source DAST engine designed to automate web application security testing through modular vulnerability detection and payload-based testing.

The project is being developed with a focus on:

* Automated vulnerability discovery
* Modular detection rules
* Reproducible security testing
* CLI-driven workflows
* Machine-readable reporting
* Developer-friendly security automation
* CI/CD integration

**Repository:** `github.com/CalculusGuy/...`

> All testing documented in this report was conducted against an intentionally vulnerable application in an authorized local environment.
