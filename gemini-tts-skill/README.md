# Gemini TTS Stability Skill

A local, cross-platform helper for diagnosing network connectivity and using Google AI Studio Generate Speech with the user's own account.

Official target: https://aistudio.google.com/generate-speech

This project does not bypass geographic eligibility, account checks, CAPTCHA, quotas, or Google security controls. It never collects Google credentials or browser cookies.

## Features
- Windows and Linux environment checks
- DNS resolution checks
- Independent IPv4 and IPv6 checks
- HTTPS reachability check for AI Studio
- Optional public egress IP check (off by default)
- Safe guidance for manual Google sign-in
- GitHub Actions egress-IP limitations and legitimate static-IP options
- Troubleshooting documentation

## Requirements
- Python 3.9+
- Windows 10/11 or mainstream Linux
- Modern browser
- Google account eligible for the relevant AI Studio feature

No third-party Python packages are required.

## Quick start

### Windows PowerShell
    py -3 scripts/check_environment.py
    py -3 scripts/network_diagnostics.py

### Linux
    python3 scripts/check_environment.py
    python3 scripts/network_diagnostics.py

Machine-readable output:
    python3 scripts/network_diagnostics.py --json

Optional public egress IP check (contacts api.ipify.org):
    python3 scripts/network_diagnostics.py --check-public-ip

## Sign in and generate speech
1. Open https://aistudio.google.com/generate-speech.
2. Sign in manually.
3. Complete any verification yourself.
4. Use Generate Speech and download the audio through the official UI.

For API-based production workflows, consult https://ai.google.dev/gemini-api/docs and use current model names and request schemas.

## GitHub IP note
A normal GitHub Actions runner does not have a fixed outbound IP. GitHub documents static public IP ranges for eligible GitHub Enterprise Cloud larger runners only. Those ranges apply to jobs on the runner; they do not change your own computer or browser IP and are not a VPN/proxy. See [docs/github-egress.md](docs/github-egress.md) before designing any allowlist workflow.

## Network configuration
The scripts are read-only. They do not modify DNS, routes, firewall rules, proxy settings, or IPv4/IPv6 configuration. DNS does not pin your public IP. For a stable public IP on your own computer, ask your ISP about a static address or use a compliant dedicated-egress service.

See docs/network.md and docs/troubleshooting.md.

## Security
- Never commit passwords, API keys, OAuth tokens, cookies, or browser profiles.
- Review diagnostic output before sharing it.
- Store API keys in environment variables or a secret manager.
- Never disable TLS certificate validation.

## License
MIT. See LICENSE.
