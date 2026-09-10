# Security Policy

Retro Game Vision is an evidence-driven data pipeline that can work with local images, structured observations, SQLite data, and marketplace-derived evidence. Security reports that could expose local data, bypass publication boundaries, or execute unintended code are taken seriously.

## Supported version

Security fixes target the current `main` branch and the latest public demo state.

## Reporting a vulnerability

Please do **not** open a public issue for a vulnerability that could expose private field data, local paths, credentials, source adapters, or other sensitive information.

Report it privately to **MarcelosOfficial@gmail.com** with the subject `Retro Game Vision security report` and include:

- affected commit or version
- clear reproduction steps
- expected versus observed behavior
- likely impact
- sanitized logs, screenshots, or sample inputs when useful

Do not include real marketplace credentials, private store evidence, or personal data in a public report.

## Scope

Examples of useful reports include:

- path traversal or arbitrary file access
- unsafe handling of image or structured-input paths
- publication-boundary bypasses that could expose private data
- SQLite injection or unsafe query construction
- secrets or sensitive source data written to logs or generated artifacts
- dependency or packaging behavior that executes untrusted content

General bugs, identification mistakes, valuation logic, and feature requests can use normal GitHub issues.