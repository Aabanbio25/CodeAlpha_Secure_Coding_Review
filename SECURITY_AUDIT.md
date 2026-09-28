\# Secure Coding Review Report



\## Identified Vulnerabilities \& Remediation



\### 1. Hardcoded API Secret Key

\- \*\*Severity:\*\* High

\- \*\*Vulnerability:\*\* Storing secrets in source code risks credentials leaking in version control.

\- \*\*Remediation:\*\* Use environment variables (`os.getenv`) to load secrets securely.



\### 2. SQL Injection (SQLi)

\- \*\*Severity:\*\* Critical

\- \*\*Vulnerability:\*\* Direct string formatting in SQL queries allows untrusted user input manipulation.

\- \*\*Remediation:\*\* Use parameterized queries with placeholders (`?`).

