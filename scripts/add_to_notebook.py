#!/usr/bin/env python3
"""Dodawanie źródeł YouTube do notatnika NotebookLM."""
import argparse
import json

try:
    from notebooklm import NotebookLM
except ImportError:
    print(json.dumps({"error": "notebooklm-py nie jest zainstalowany"}))
    raise SystemExit(1)

parser = argparse.ArgumentParser()
parser.add_argument("--notebook-id", required=True)
parser.add_argument("--urls", required=True, help="JSON array lub pojedynczy URL")
args = parser.parse_args()

try:
    urls = json.loads(args.urls) if args.urls.startswith("[") else [args.urls]
except json.JSONDecodeError:
    urls = [u.strip() for u in args.urls.split(",")]

try:
    client = NotebookLM()
    notebook = client.get_notebook(args.notebook_id)
except Exception as e:
    print(json.dumps({"error": f"Nie można otworzyć notatnika: {e}"}))
    raise SystemExit(1)

results = []
for url in urls:
    try:
        notebook.add_source(url)
        results.append({"url": url, "status": "added"})
        print(json.dumps({"url": url, "status": "added"}), flush=True)
    except Exception as e:
        err = str(e)
        results.append({"url": url, "status": "error", "reason": err})
        print(json.dumps({"url": url, "status": "error", "reason": err}), flush=True)

summary = {
    "added": sum(1 for r in results if r["status"] == "added"),
    "failed": sum(1 for r in results if r["status"] != "added"),
    "total": len(results),
}
print(json.dumps({"summary": summary}))
