#!/usr/bin/env python3
"""Tworzenie notatnika w NotebookLM."""
import argparse
import json
import datetime
from pathlib import Path

try:
    from notebooklm import NotebookLM
except ImportError:
    print(json.dumps({"error": "notebooklm-py nie jest zainstalowany"}))
    raise SystemExit(1)

parser = argparse.ArgumentParser()
parser.add_argument("--title", required=True)
parser.add_argument("--description", default="")
args = parser.parse_args()

try:
    client = NotebookLM()
    notebook = client.create_notebook(title=args.title, description=args.description)
    meta = {"id": notebook.id, "title": notebook.title, "created": str(datetime.date.today())}

    notebooks_dir = Path(__file__).parent.parent / "notebooks"
    notebooks_dir.mkdir(exist_ok=True)
    (notebooks_dir / f"{notebook.id}.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2)
    )

    import yaml
    cfg_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    cfg = yaml.safe_load(cfg_path.read_text()) if cfg_path.exists() else {}
    cfg.setdefault("notebook", {}).update(meta)
    cfg_path.write_text(yaml.dump(cfg, allow_unicode=True))

    print(json.dumps(meta, ensure_ascii=False))
except Exception as e:
    print(json.dumps({"error": str(e)}))
    raise SystemExit(1)
