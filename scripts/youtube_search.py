#!/usr/bin/env python3
"""Wyszukiwanie wideo na YouTube."""
import argparse
import json
import sys


def parse_views(text: str) -> int:
    if not text:
        return 0
    cleaned = text.replace(",", "").replace(".", "").replace(" ", "").lower()
    for suffix, mult in [("b", 1_000_000_000), ("m", 1_000_000), ("k", 1_000)]:
        if cleaned.endswith(suffix):
            try:
                return int(float(cleaned[:-1]) * mult)
            except ValueError:
                return 0
    try:
        return int(cleaned)
    except ValueError:
        return 0


def search(topic: str, lang: str = "en", max_results: int = 10, min_views: int = 1000) -> list:
    try:
        from youtubesearchpython import VideosSearch
    except ImportError:
        print(json.dumps({"error": "Brak youtube-search-python. Uruchom: pip3 install youtube-search-python"}))
        sys.exit(1)

    query = topic if lang != "pl" else f"{topic} po polsku"
    try:
        results = VideosSearch(query, limit=max_results * 2).result().get("result", [])
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    videos = []
    for item in results:
        views = parse_views(item.get("viewCount", {}).get("text", "0"))
        if views < min_views:
            continue
        videos.append({
            "title": item.get("title", ""),
            "url": f"https://youtube.com/watch?v={item.get('id', '')}",
            "channel": item.get("channel", {}).get("name", ""),
            "views": views,
            "duration": item.get("duration", ""),
            "description": (item.get("descriptionSnippet") or [{}])[0].get("text", ""),
        })
        if len(videos) >= max_results:
            break

    return videos


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--lang", default="en")
    parser.add_argument("--max", type=int, default=10)
    parser.add_argument("--min-views", type=int, default=1000)
    args = parser.parse_args()

    results = search(args.topic, args.lang, args.max, args.min_views)
    print(json.dumps(results, ensure_ascii=False, indent=2))
