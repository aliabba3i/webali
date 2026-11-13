# Troubleshooting

## AI Studio page does not load
- Run the diagnostics script.
- Check DNS resolution over IPv4 and IPv6 separately.
- An HTTP 403/404 still means an HTTP server was reached; it does not mean the feature is available.
- Check local firewall, router, ISP, system clock, and TLS trust.

## Google sign-in loops or verification appears
- Sign in and complete verification manually in the browser.
- Check system date and time.
- Do not copy cookies, automate OTP entry, spoof fingerprints, or use CAPTCHA-solving services.

## Region or account eligibility message
This is an account/service availability decision, not a DNS problem. Stop network workarounds and check Google's current supported regions and account requirements.

## Quota or rate limit
Stop retrying. Check quota and billing status, wait for the documented reset, or use an authorized quota option.

## IPv4 works but IPv6 fails (or the reverse)
Record the result and inspect router/ISP configuration. Do not disable a protocol globally without a diagnosed reason and administrator approval.

## TLS or certificate error
Check device time, OS trust store, corporate TLS inspection, and security software. Never disable certificate validation.
