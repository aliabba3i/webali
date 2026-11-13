---
name: gemini-tts-stability
description: Diagnose network and browser-session issues and assist with Google AI Studio Generate Speech using the user's own account.
---

# Gemini TTS Stability Skill

## Goal
Help the user access https://aistudio.google.com/generate-speech and generate speech with their own Google account. Diagnose DNS, IPv4, IPv6, HTTPS, and browser-session issues on Windows and Linux.

## Boundaries
- Do not bypass Google's regional eligibility, account checks, CAPTCHA, quotas, rate limits, or security controls.
- Do not spoof location, rotate proxies to evade restrictions, forge browser fingerprints, or automate credential/OTP entry.
- Never request, store, print, or commit passwords, cookies, OAuth tokens, or browser profiles.
- The user completes Google sign-in and security verification manually in their browser.
- Do not change DNS, routes, firewall, proxy, or IPv4/IPv6 settings without explaining the exact change and receiving explicit approval.
- DNS does not make a public IP static. A stable public IP requires an ISP static-IP service or dedicated static egress.
- Prefer official Gemini API workflows when suitable; check current official documentation for model names and schemas.

## Workflow
1. Identify OS and browser; do not assume.
2. Run scripts/network_diagnostics.py. Use --json for structured output.
3. Compare IPv4 and IPv6 DNS results and HTTPS reachability.
4. Open the official AI Studio URL; user signs in manually.
5. If access is denied for region/account eligibility, stop and explain supported access options.
6. If quota/rate limit is reached, stop retries and follow the documented reset or authorized billing/quota path.
7. For transient network failures, use bounded retries with exponential backoff.
8. Save audio using the official UI or an authorized API workflow.

## Error classification
- DNS / TCP / TLS: diagnose local resolver, router, ISP, firewall, system clock, and certificate trust.
- Sign-in / verification: user completes the official flow.
- Region / eligibility: not a DNS issue; do not evade.
- Quota / rate limit: wait or use authorized quota options.
- Invalid input / unsupported voice: validate against the current UI or official docs.

## Repository contents
- scripts/network_diagnostics.py: read-only DNS, IPv4, IPv6 and HTTPS checks.
- scripts/check_environment.py: local prerequisite check.
- docs/network.md: safe network guidance.
- docs/troubleshooting.md: decision tree.

## Definition of done
The user can reach the official page, sign in manually, view network diagnostics, and generate/download audio through an officially supported path without bypassing access controls.
