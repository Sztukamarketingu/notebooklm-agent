# NotebookLM YouTube Research Agent

Agent dla Claude Code, który automatycznie zbiera najlepsze materiały wideo z YouTube na wybrany temat, buduje z nich bazę wiedzy w NotebookLM i zapisuje notatki w Obsidian — tworząc osobistą bibliotekę wiedzy gotową do odpytywania i nauki.

**Przykład użycia:** zbierz 10 materiałów o strategiach marketingowych → zapytaj NotebookLM „Jakie są najskuteczniejsze strategie pozyskiwania klientów w 2024?" → przeglądaj połączone notatki i ucz się z flashcards w Obsidian.

---

## Jak to działa

```
YouTube ──────► NotebookLM ──────► Obsidian
   │                  │                 │
Wyszukujesz       Zadajesz         Notatki MD
temat             pytania AI       per wideo
   │                  │                 │
Agent zbiera      "Jaką strategię   MOC z grafem
10 najlepszych    wybrać?"          powiązań
wideo                               │
                                Flashcards
                                do nauki
```

1. **YouTube** — agent wyszukuje i filtruje wideo według tematu, języka i liczby wyświetleń
2. **NotebookLM** — wideo trafiają jako źródła do notatnika; możesz zadawać pytania AI na podstawie transkryptów
3. **Obsidian** — każda sesja tworzy notatki Markdown w Twoim vault'cie, które z czasem budują osobistą bazę wiedzy z grafem powiązań i kartami do nauki

---

## Wymagania

- [Claude Code](https://claude.ai/download) — bezpłatny
- [Python 3.9+](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org) — do instalacji skilli
- Konto Google — do NotebookLM
- [Obsidian](https://obsidian.md) — bezpłatny, opcjonalny

---

## Instalacja

### 1. Pobierz projekt

**Opcja A – ZIP** *(łatwiejsza, bez znajomości Git)*
1. Kliknij zielony przycisk **Code → Download ZIP**
2. Rozpakuj folder w dowolnym miejscu na komputerze

**Opcja B – terminal**
```bash
git clone https://github.com/Sztukamarketingu/notebooklm-agent.git
```

### 2. Otwórz w Claude Code

Otwórz Claude Code i przejdź do pobranego folderu.

### 3. Uruchom setup

Wpisz w Claude Code:
```
/setup
```

Agent przeprowadzi Cię przez wszystkie kroki: instalację bibliotek, logowanie do NotebookLM oraz instalację skilli.

---

## Komendy

| Komenda | Co robi |
|---|---|
| `/setup` | Pierwsza konfiguracja — instalacja wszystkiego |
| `/research` | Pełny workflow: YouTube → NotebookLM → Obsidian |
| `/compare` | Porównaj dwóch twórców — debata perspektyw w jednym notatniku |
| `/youtube-search` | Wyszukaj wideo i podejrzyj wyniki |
| `/create-notebook` | Stwórz nowy notatnik w NotebookLM |
| `/add-to-notebook` | Dodaj wideo do istniejącego notatnika |
| `/obsidian` | Eksportuj sesję do Obsidian |

---

## Przykładowa sesja

```
Ty:    /research
Agent: Czego będziemy szukać?
Ty:    strategie marketingu w social media
Agent: Znalazłem 10 wideo. Tworzę notatnik "strategie marketingu – 2024-04-07"...
       [1/10] ✓ "Social Media Strategy 2024" – Neil Patel
       [2/10] ✓ "Content Marketing Masterclass" – HubSpot
       ...
       Gotowe! 9/10 wideo dodanych do NotebookLM.
       Możesz teraz zapytać: "Jakie błędy popełniają marki na Instagramie?"

       Czy chcesz zapisać materiały w Obsidian?
Ty:    tak, i zrób flashcards
Agent: Tworzę notatki w vault...
       ✓ 9 notatek MD
       ✓ _MOC.md (mapa tematu z linkami)
       ✓ _Flashcards.md (gotowe do nauki w Obsidian)
```

---

## Porównanie perspektyw — `/compare`

Chcesz wiedzieć jak dany temat widzi ekspert A, a jak ekspert B? Komenda `/compare` zbiera wideo od dwóch twórców, wrzuca je do jednego notatnika NotebookLM i generuje gotowe pytania do debaty.

```
Ty:    /compare
Agent: Na jaki temat? I którzy dwaj twórcy?
Ty:    strategie reklamowe — Neil Patel i Gary Vaynerchuk
Agent: Szukam wideo Neil Patel o strategiach reklamowych... (5 wideo)
       Szukam wideo Gary Vaynerchuk o strategiach reklamowych... (5 wideo)
       Tworzę notatnik "Neil Patel vs Gary Vaynerchuk: strategie reklamowe"...
       Dodaję 10 wideo...

       Gotowe! Przykładowe pytania do NotebookLM:
       → "Jak Neil Patel i Gary Vaynerchuk różnią się w podejściu do Facebook Ads?"
       → "Gdyby obaj doradzali mojej firmie, na co by się zgodzili?"
       → "Jaką strategię poleciłby Neil Patel dla e-commerce?"
```

W Obsidian tworzy się notatka z sekcjami: **Perspektywa A**, **Perspektywa B**, **Punkty sporu**, **Punkty zgody** i **Mój wniosek** — gotowa do własnych przemyśleń.

---

## Obsidian — jak to działa

Po wpisaniu `/obsidian` (lub automatycznie po `/research`) agent tworzy w Twoim vault'cie:

```
vault/
└── NotebookLM/
    └── strategie marketingu/
        ├── _MOC.md              ← mapa tematu, linki do wszystkich wideo
        ├── _Flashcards.md       ← karty do nauki (plugin Spaced Repetition)
        ├── Social Media Strategy 2024.md
        ├── Content Marketing Masterclass.md
        └── ...
```

**Każda notatka zawiera:** kanał, link, liczba wyświetleń, opis, miejsce na własne przemyślenia i tagi.

**Graf powiązań** (`Ctrl+G` w Obsidian) pokazuje połączenia między tematami i twórcami — im więcej sesji badawczych, tym bogatszy graf.

**Flashcards** są kompatybilne z pluginem [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) — otwórz `_Flashcards.md` i kliknij "Review flashcards".

Ścieżka do vault'u jest zapamiętywana w `config/settings.yaml` — nie musisz jej podawać za każdym razem.

---

## Bezpieczeństwo

- Dane logowania do Google przechowuje lokalnie Playwright — nie trafiają nigdzie indziej
- Folder `config/credentials/` jest w `.gitignore`
- Żadne dane nie są wysyłane poza Twój komputer, NotebookLM i YouTube
