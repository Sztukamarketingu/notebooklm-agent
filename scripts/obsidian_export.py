#!/usr/bin/env python3
"""Eksport wyników badań do Obsidian vault."""
import argparse
import json
import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent


def load_videos(topic: str) -> list[dict]:
    """Wczytaj ostatnie wyniki z transcripts/ lub settings.yaml."""
    transcripts_dir = ROOT / "transcripts"
    safe = "".join(c if c.isalnum() or c in " _-" else "_" for c in topic)[:60]
    path = transcripts_dir / f"{safe}.json"
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        return data.get("videos", [])
    # fallback: spróbuj wczytać ostatni plik w transcripts/
    files = sorted(transcripts_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if files:
        data = json.loads(files[0].read_text(encoding="utf-8"))
        return data.get("videos", [])
    return []


def save_vault_path(vault_path: str) -> None:
    cfg_path = ROOT / "config" / "settings.yaml"
    cfg = yaml.safe_load(cfg_path.read_text()) if cfg_path.exists() else {}
    cfg.setdefault("obsidian", {})["vault_path"] = vault_path
    cfg_path.write_text(yaml.dump(cfg, allow_unicode=True))


def make_safe_filename(title: str, max_len: int = 80) -> str:
    forbidden = r'\/:*?"<>|'
    cleaned = "".join(c if c not in forbidden else "_" for c in title)
    return cleaned[:max_len].strip()


def export(vault_path: str, topic: str, flashcards: bool = False) -> dict:
    vault = Path(vault_path)
    if not vault.exists():
        return {"error": f"Vault nie istnieje: {vault_path}"}

    save_vault_path(vault_path)

    videos = load_videos(topic)
    if not videos:
        return {"error": "Brak wideo do eksportu. Najpierw uruchom /research."}

    safe_topic = make_safe_filename(topic)
    output_dir = vault / "NotebookLM" / safe_topic
    output_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.date.today().isoformat()
    created = 0
    updated = 0
    note_links = []

    for video in videos:
        if video.get("status") not in ("added", None, ""):
            continue

        title = video.get("title", "Bez tytułu")
        safe_title = make_safe_filename(title)
        note_path = output_dir / f"{safe_title}.md"

        views_str = f"{video.get('views', 0):,}".replace(",", " ")
        tag_topic = safe_topic.replace(" ", "_").lower()
        tag_channel = make_safe_filename(video.get("channel", "")).replace(" ", "_").lower()

        content = (
            f"# {title}\n\n"
            f"## Metadane\n"
            f"- **Kanał:** {video.get('channel', '')}\n"
            f"- **Link:** {video.get('url', '')}\n"
            f"- **Wyświetlenia:** {views_str}\n"
            f"- **Czas trwania:** {video.get('duration', '')}\n"
            f"- **Dodano:** {today}\n\n"
            f"## Opis\n\n{video.get('description', '')}\n\n"
            f"## Kluczowe wnioski\n\n"
            f"> *(uzupełnij po obejrzeniu lub zapytaj NotebookLM o podsumowanie)*\n\n"
            f"## Moje notatki\n\n\n\n"
            f"## Powiązane tematy\n\n"
            f"[[{safe_topic}/_MOC]]\n\n"
            f"#notebooklm #{tag_topic} #{tag_channel}\n"
        )

        if note_path.exists():
            updated += 1
        else:
            created += 1

        note_path.write_text(content, encoding="utf-8")
        note_links.append(f"- [[{safe_title}]] — {video.get('channel', '')}")

    # MOC (Map of Content)
    moc_path = output_dir / "_MOC.md"
    moc_content = (
        f"# {topic}\n\n"
        f"Baza wiedzy zbudowana: {today}\n"
        f"Źródła: {len(note_links)} wideo z YouTube\n\n"
        f"## Wideo\n\n"
        + "\n".join(note_links) + "\n\n"
        f"## Pytania do NotebookLM\n\n"
        f"*(skopiuj i wklej na notebooklm.google.com)*\n\n"
        f"- Jakie są najważniejsze wnioski z tych materiałów?\n"
        f"- Jakie strategie są wspólne dla większości twórców?\n"
        f"- Jakie błędy najczęściej się pojawiają?\n"
        f"- Porównaj podejścia różnych ekspertów.\n\n"
        f"#notebooklm #{safe_topic.replace(' ', '_').lower()}\n"
    )
    moc_path.write_text(moc_content, encoding="utf-8")

    # Flashcards
    if flashcards:
        fc_path = output_dir / "_Flashcards.md"
        fc_lines = [
            "# Flashcards — " + topic,
            "",
            "> Kompatybilne z pluginem **Spaced Repetition** (obsidian-spaced-repetition)",
            "",
            "## Jak używać",
            "1. Zainstaluj plugin: Obsidian → Community plugins → Spaced Repetition",
            "2. Otwórz ten plik i kliknij 'Review flashcards'",
            "",
            "---",
            "",
        ]
        for video in videos:
            title = video.get("title", "")
            channel = video.get("channel", "")
            if title:
                fc_lines += [
                    f"#flashcard",
                    f"",
                    f"**Q:** O czym jest materiał „{title}" od {channel}?",
                    f"",
                    f"**A:** [uzupełnij po obejrzeniu lub zapytaj NotebookLM]",
                    f"",
                    f"---",
                    f"",
                ]
        fc_path.write_text("\n".join(fc_lines), encoding="utf-8")

    return {
        "created": created,
        "updated": updated,
        "total": created + updated,
        "path": str(output_dir),
        "moc": str(moc_path),
        "flashcards": str(fc_path) if flashcards else None,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault-path", required=True)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--flashcards", action="store_true")
    args = parser.parse_args()

    result = export(args.vault_path, args.topic, args.flashcards)
    print(json.dumps(result, ensure_ascii=False, indent=2))
