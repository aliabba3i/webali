---
name: gemini-tts-stability
description: Diagnose Google AI Studio Generate Speech access and network issues. Use for Persian TTS workflows, DNS, IPv4, IPv6, HTTPS checks, and safe Windows/Linux setup.
---

# Gemini TTS Stability

Use this skill to help the user work with https://aistudio.google.com/generate-speech.

## First steps
1. Identify the user's OS if not already known.
2. Read gemini-tts-skill/README.md.
3. Run the read-only diagnostic script:
   - Windows: py -3 gemini-tts-skill/scripts/network_diagnostics.py
   - Linux: python3 gemini-tts-skill/scripts/network_diagnostics.py
4. For structured output, add --json.
5. Check public egress IP only if the user explicitly opts in: add --check-public-ip.

## Safe authentication
The user signs in manually in the official browser. Never request or store passwords, one-time codes, cookies, OAuth tokens, or browser profile data. Do not automate CAPTCHA or verification.

## Network policy
Diagnose DNS, IPv4, IPv6, HTTPS, TLS, firewall, router, and ISP issues independently. Do not change network settings without explaining the exact change and receiving approval. DNS does not make a public IP static. A static public IP must come from the ISP or a legitimate dedicated-egress provider.

### GitHub Actions IP behavior
Standard GitHub-hosted runners use changing outbound IP addresses; a repository does not receive a dedicated fixed IP. GitHub documents static IP ranges for eligible GitHub Enterprise Cloud larger runners only. These ranges are the egress of the runner jobs, not the user's computer or browser. Do not implement a proxy, VPN, or traffic relay to route AI Studio browser traffic through GitHub or disguise location. Read gemini-tts-skill/docs/github-egress.md.

## Access restrictions
Do not bypass geographic eligibility, account checks, CAPTCHA, quotas, rate limits, or security controls. Do not spoof location, rotate proxies to evade restrictions, or forge browser fingerprints. For a region/account eligibility message, stop and direct the user to Google's supported availability information. For quota errors, stop retries and use the documented reset or authorized quota path.

## Speech generation
Use the official AI Studio interface or an authorized Gemini API workflow. Verify current API model identifiers and schemas in Google's official documentation before implementing API calls. Save audio through the official UI or supported API response handling.

## Troubleshooting
Consult gemini-tts-skill/docs/troubleshooting.md, gemini-tts-skill/docs/network.md, and gemini-tts-skill/docs/github-egress.md. Keep retries bounded and only retry transient network errors.
