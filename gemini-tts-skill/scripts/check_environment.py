#!/usr/bin/env python3
"""Check local prerequisites without changing system settings."""
import importlib.util
import platform
import shutil
import sys

print("Gemini TTS Stability - environment check")
print("OS:", platform.platform())
print("Python:", sys.version.split()[0])
print("Python 3.9+:", sys.version_info >= (3, 9))
browsers = ("chrome", "google-chrome", "chromium", "chromium-browser", "msedge", "firefox")
found = [name for name in browsers if shutil.which(name)]
print("Browser commands:", ", ".join(found) if found else "none found on PATH")
print("Playwright installed:", bool(importlib.util.find_spec("playwright")))
print("No system settings were changed.")
