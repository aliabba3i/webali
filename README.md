# Webali repository

## Gemini TTS Stability Skill

A cross-platform skill and diagnostic toolkit for Google AI Studio Generate Speech.

- Skill instructions: [gemini-tts-skill/SKILL.md](gemini-tts-skill/SKILL.md)
- Setup and usage: [gemini-tts-skill/README.md](gemini-tts-skill/README.md)
- Network diagnostics: [network_diagnostics.py](gemini-tts-skill/scripts/network_diagnostics.py)
- GitHub Actions IP behavior: [github-egress.md](gemini-tts-skill/docs/github-egress.md)

Quick start:

Windows:
    py -3 gemini-tts-skill/scripts/network_diagnostics.py

Linux:
    python3 gemini-tts-skill/scripts/network_diagnostics.py

The toolkit diagnoses connectivity; it does not bypass Google eligibility, account security, CAPTCHA, quota, or rate limits. Standard GitHub Actions runners do not provide a fixed outbound IP.
