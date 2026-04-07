# NotebookLM YouTube Research Agent

Automatycznie zbiera najlepsze materiały wideo z YouTube na wybrany temat, buduje bazę wiedzy w NotebookLM i zapisuje notatki w Obsidian — tworząc osobistą bibliotekę wiedzy gotową do odpytywania i nauki.

**Przykład użycia:** zbierz 10 materiałów o strategiach marketingowych → zapytaj NotebookLM „Jakie są najskuteczniejsze strategie pozyskiwania klientów?" → przeglądaj notatki i flashcards w Obsidian

---

## Wymagania

- [Claude Code](https://claude.ai/download) (bezpłatny)
- [Python 3.9+](https://www.python.org/downloads/)
- Konto Google (do NotebookLM)
- [Obsidian](https://obsidian.md) — bezpłatny, opcjonalny (do notatek i nauki)

---

## Instalacja

### 1. Pobierz projekt

**Opcja A – pobierz ZIP** *(łatwiejsza)*
1. Kliknij zielony przycisk **Code → Download ZIP**
2. Rozpakuj folder w dowolnym miejscu

**Opcja B – git clone**
```bash
git clone https://github.com/TWOJ_USERNAME/notebooklm-agent.git
```

### 2. Otwórz w Claude Code

Otwórz Claude Code i przejdź do pobranego folderu.

### 3. Uruchom setup

W Claude Code wpisz:
```
/setup
```

Agent przeprowadzi Cię przez instalację krok po kroku.

---

## Jak używać

Po konfiguracji masz do dyspozycji komendy:

| Komenda | Co robi |
|---|---|
| `/research` | Pełny workflow: szukaj → notatnik → Obsidian |
| `/youtube-search` | Wyszukaj wideo (podgląd bez dodawania) |
| `/create-notebook` | Stwórz nowy notatnik w NotebookLM |
| `/add-to-notebook` | Dodaj wideo do istniejącego notatnika |
| `/obsidian` | Eksportuj notatki do Obsidian + flashcards do nauki |

### Przykładowa sesja

```
Ty:    /research
Agent: Czego będziemy szukać?
Ty:    strategie marketingu w social media
Agent: [wyszukuje 10 wideo, tworzy notatnik, dodaje źródła]
Agent: Gotowe! Twój notatnik: notebooklm.google.com
       Przykładowe pytania: "Jakie błędy popełniają marki na Instagramie?"
       Czy chcesz zapisać materiały w Obsidian?
Ty:    tak
Agent: [tworzy notatki w vault + flashcards do nauki]
```

---

## Struktura projektu

```
.claude/
  CLAUDE.md              # Definicja agenta
  commands/              # Slash commands
    setup.md
    research.md
    youtube-search.md
    create-notebook.md
    add-to-notebook.md
    obsidian.md
scripts/                 # Skrypty pomocnicze Python
config/
  settings.yaml          # Stan i konfiguracja (vault path, notebook id…)
notebooks/               # Metadane notatników NotebookLM
transcripts/             # Lokalne kopie wyników sesji
requirements.txt
```

---

## Bezpieczeństwo

- Dane logowania do Google są przechowywane lokalnie przez Playwright (nie trafiają nigdzie indziej)
- Folder `config/credentials/` jest w `.gitignore`
