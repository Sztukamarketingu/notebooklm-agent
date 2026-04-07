# NotebookLM YouTube Research Agent

Automatycznie zbiera najlepsze materiały wideo z YouTube na wybrany temat i buduje z nich bazę wiedzy w NotebookLM, którą możesz odpytywać.

**Przykład użycia:** zbierz 10 najlepszych materiałów o strategiach marketingowych → zapytaj „Jakie są najskuteczniejsze strategie pozyskiwania klientów?"

---

## Wymagania

- [Claude Code](https://claude.ai/download) (bezpłatny)
- [Python 3.9+](https://www.python.org/downloads/)
- Konto Google (do NotebookLM)

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
| `/research` | Pełny workflow: szukaj → buduj notatnik → gotowe |
| `/youtube-search` | Wyszukaj wideo (podgląd bez dodawania) |
| `/create-notebook` | Stwórz nowy notatnik w NotebookLM |
| `/add-to-notebook` | Dodaj wideo do istniejącego notatnika |

### Przykładowa sesja

```
Ty: /research
Agent: Czego będziemy szukać?
Ty: strategie marketingu w social media
Agent: [wyszukuje 10 wideo, tworzy notatnik, dodaje źródła]
Agent: Gotowe! Twój notatnik jest na notebooklm.google.com
       Możesz zapytać np. "Jakie błędy najczęściej popełniają marki na Instagramie?"
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
scripts/                 # Skrypty pomocnicze
config/
  settings.yaml          # Stan i konfiguracja
notebooks/               # Metadane notatników
transcripts/             # Lokalne wyniki
requirements.txt
```

---

## Bezpieczeństwo

- Dane logowania do Google są przechowywane lokalnie przez Playwright (nie trafiają nigdzie indziej)
- Folder `config/credentials/` jest w `.gitignore`
