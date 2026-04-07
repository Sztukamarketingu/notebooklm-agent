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
GLOBAL_COMMANDS = Path.home() / ".claude" / "commands"
SCRIPTS_SRC = PROJECT_ROOT / "scripts"
GLOBAL_SCRIPTS = Path.home() / ".claude" / "notebooklm-scripts"
SETTINGS_FILE = Path.home() / ".claude" / "notebooklm_config.json"


def main():
    # Utwórz globalny folder komend jeśli nie istnieje
    GLOBAL_COMMANDS.mkdir(parents=True, exist_ok=True)

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
