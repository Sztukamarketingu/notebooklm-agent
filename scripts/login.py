#!/usr/bin/env python3
"""Logowanie do NotebookLM przez przeglądarkę."""
try:
    from notebooklm import NotebookLM
except ImportError:
    print("Błąd: notebooklm-py nie jest zainstalowany.")
    print("Uruchom: pip3 install 'notebooklm-py[browser]'")
    raise SystemExit(1)

print("Otwieram przeglądarkę Chromium...")
print("Zaloguj się kontem Google używanym na notebooklm.google.com")
print("Po zalogowaniu wróć tutaj.\n")

try:
    client = NotebookLM(browser_login=True)
    print("Logowanie zakończone pomyślnie!")
except Exception as e:
    print(f"Błąd logowania: {e}")
    raise SystemExit(1)
