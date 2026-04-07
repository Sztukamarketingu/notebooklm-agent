#!/usr/bin/env python3
"""
Kopiuje komendy agenta do globalnego folderu ~/.claude/commands/
żeby działały w każdym projekcie Claude Code.
"""
import shutil
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
COMMANDS_SRC = PROJECT_ROOT / ".claude" / "commands"
CLAUDE_MD_SRC = PROJECT_ROOT / ".claude" / "CLAUDE.md"
GLOBAL_CLAUDE = Path.home() / ".claude"
GLOBAL_COMMANDS = GLOBAL_CLAUDE / "commands"
SCRIPTS_SRC = PROJECT_ROOT / "scripts"
GLOBAL_SCRIPTS = GLOBAL_CLAUDE / "notebooklm-scripts"
SETTINGS_FILE = GLOBAL_CLAUDE / "notebooklm_config.json"


def main():
    # Utwórz globalne foldery
    GLOBAL_COMMANDS.mkdir(parents=True, exist_ok=True)

    # Skopiuj CLAUDE.md globalnie (persona agenta działa wszędzie)
    global_claude_md = GLOBAL_CLAUDE / "CLAUDE.md"
    if global_claude_md.exists():
        # Nie nadpisuj jeśli użytkownik ma własny CLAUDE.md — dołącz na końcu
        existing = global_claude_md.read_text(encoding="utf-8")
        agent_md = CLAUDE_MD_SRC.read_text(encoding="utf-8")
        marker = "# NotebookLM YouTube Research Agent"
        if marker not in existing:
            global_claude_md.write_text(existing + "\n\n---\n\n" + agent_md, encoding="utf-8")
            print(f"  ✓ CLAUDE.md → dołączono do istniejącego {global_claude_md}")
        else:
            print(f"  ✓ CLAUDE.md → już zainstalowany, pomijam")
    else:
        shutil.copy2(CLAUDE_MD_SRC, global_claude_md)
        print(f"  ✓ CLAUDE.md → {global_claude_md}")

    # Skopiuj wszystkie pliki .md z komendami
    copied = []
    for cmd_file in COMMANDS_SRC.glob("*.md"):
        dest = GLOBAL_COMMANDS / cmd_file.name
        shutil.copy2(cmd_file, dest)
        copied.append(cmd_file.name)
        print(f"  ✓ {cmd_file.name} → {dest}")

    # Skopiuj skrypty pomocnicze
    if GLOBAL_SCRIPTS.exists():
        shutil.rmtree(GLOBAL_SCRIPTS)
    shutil.copytree(SCRIPTS_SRC, GLOBAL_SCRIPTS)
    print(f"  ✓ scripts/ → {GLOBAL_SCRIPTS}")

    # Zapisz ścieżkę do skryptów żeby komendy wiedziały gdzie ich szukać
    config = {
        "scripts_path": str(GLOBAL_SCRIPTS),
        "project_path": str(PROJECT_ROOT),
    }
    SETTINGS_FILE.write_text(json.dumps(config, indent=2))
    print(f"  ✓ config → {SETTINGS_FILE}")

    print(f"\nZainstalowano {len(copied)} komend globalnie.")
    print(f"Dostępne z każdego folderu: {', '.join(f'/{f.replace('.md', '')}' for f in copied)}")


if __name__ == "__main__":
    main()
