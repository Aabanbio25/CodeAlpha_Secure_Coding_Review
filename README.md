# CodeAlpha - Secure Coding Review

A security audit and code review project demonstrating vulnerable Python code alongside remediated secure code and audit documentation. Developed as part of the **CodeAlpha Cybersecurity Internship Program**.

## Project Files
- `app_vulnerable.py`: Demonstrates common security risks (Hardcoded Secrets & SQL Injection).
- `app_secure.py`: Demonstrates remediated code using environment variables and parameterized queries.
- `SECURITY_AUDIT.md`: Complete security audit report detailing vulnerabilities and fixes.

## Key Security Improvements
1. **Secrets Management:** Moved API credentials from hardcoded strings to system environment variables.
2. **SQL Injection Mitigation:** Replaced string formatting with parameterized database queries.
