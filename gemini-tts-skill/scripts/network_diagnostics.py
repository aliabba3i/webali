#!/usr/bin/env python3
"""Read-only DNS, IPv4, IPv6 and HTTPS diagnostics for Google AI Studio."""
from __future__ import annotations

import argparse
import json
import platform
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request


HOST = "aistudio.google.com"
URL = "https://aistudio.google.com/generate-speech"
PUBLIC_IP_URL = "https://api.ipify.org"


def resolve(family: int) -> dict:
    try:
        rows = socket.getaddrinfo(HOST, 443, family, socket.SOCK_STREAM)
        addresses = sorted({row[4][0] for row in rows})
        return {"status": "ok" if addresses else "no_records", "addresses": addresses}
    except socket.gaierror as exc:
        return {"status": "error", "error": str(exc)}


def check_https() -> dict:
    request = urllib.request.Request(URL, headers={"User-Agent": "Gemini-TTS-Stability/1.0"})
    started = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            return {"status": "ok", "http_status": response.status,
                    "elapsed_ms": round((time.monotonic() - started) * 1000)}
    except urllib.error.HTTPError as exc:
        return {"status": "http_response", "http_status": exc.code,
                "elapsed_ms": round((time.monotonic() - started) * 1000)}
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError) as exc:
        return {"status": "error", "error": str(getattr(exc, "reason", exc)),
                "elapsed_ms": round((time.monotonic() - started) * 1000)}


def check_public_ip() -> dict:
    try:
        request = urllib.request.Request(PUBLIC_IP_URL, headers={"User-Agent": "Gemini-TTS-Stability/1.0"})
        with urllib.request.urlopen(request, timeout=8) as response:
            value = response.read(128).decode("ascii", errors="replace").strip()
        socket.inet_pton(socket.AF_INET if "." in value else socket.AF_INET6, value)
        return {"status": "ok", "public_egress_ip": value,
                "note": "May be dynamic; this does not establish that the IP is static."}
    except Exception as exc:
        return {"status": "error", "error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    parser.add_argument("--check-public-ip", action="store_true",
                        help="Opt in to contacting api.ipify.org")
    args = parser.parse_args()
    result = {
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "target": HOST,
        "dns": {
            "ipv4": resolve(socket.AF_INET),
            "ipv6": resolve(socket.AF_INET6),
        },
        "https": check_https(),
        "public_ip": check_public_ip() if args.check_public_ip else {
            "status": "skipped", "reason": "Pass --check-public-ip to opt in."
        },
        "safety": "Read-only checks. No network settings were changed."
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("Google AI Studio network diagnostics")
        print("=" * 38)
        print("Platform:", result["platform"])
        print("Python:", result["python"])
        for family in ("ipv4", "ipv6"):
            item = result["dns"][family]
            print(f"{family.upper()} DNS: {item['status']} {item.get('addresses', item.get('error', ''))}")
        print("HTTPS:", result["https"])
        print("Public IP:", result["public_ip"])
        print(result["safety"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
