#!/usr/bin/env python3
"""Zapisuje wyniki sesji badawczej lokalnie w transcripts/."""
import argparse
import json
import datetime
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--topic", required=True)
parser.add_argument("--videos", required=True, help="JSON array wideo")
args = parser.parse_args()

transcripts_dir = Path(__file__).parent.parent / "transcripts"
transcripts_dir.mkdir(exist_ok=True)

safe = "".join(c if c.isalnum() or c in " _-" else "_" for c in args.topic)[:60]
out_path = transcripts_dir / f"{safe}.json"

try:
    videos = json.loads(args.videos)
except json.JSONDecodeError:
    videos = []

data = {
    "topic": args.topic,
    "date": str(datetime.date.today()),
    "videos": videos,
}
out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"saved": str(out_path), "count": len(videos)}))
