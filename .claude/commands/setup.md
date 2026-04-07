Przeprowadź użytkownika przez pierwszą konfigurację środowiska. Wykonaj poniższe kroki po kolei, weryfikując każdy.

## KROK 1 — Sprawdź Python

Uruchom:
```
python3 --version
```

Jeśli wersja jest niższa niż 3.9 lub Python nie istnieje — poinformuj użytkownika i wyjaśnij jak zainstalować Python ze strony python.org. Zatrzymaj się tutaj.

Jeśli OK — przejdź dalej.

## KROK 2 — Zainstaluj zależności

Uruchom:
```
pip3 install -r requirements.txt
```

Jeśli błąd — spróbuj z flagą `--user`:
```
pip3 install --user -r requirements.txt
```

## KROK 3 — Zainstaluj przeglądarkę Chromium

```
python3 -m playwright install chromium
```

Jeśli błąd "with-deps":
```
python3 -m playwright install --with-deps chromium
```

## KROK 4 — Weryfikacja

Uruchom:
```
python3 -c "import notebooklm; print('notebooklm-py:', notebooklm.__version__)"
python3 -c "from youtubesearchpython import VideosSearch; print('youtube-search: OK')"
```

Jeśli oba komunikaty się wyświetliły — instalacja zakończona.

## KROK 5 — Logowanie do NotebookLM

Poinformuj użytkownika:

> Za chwilę otworzy się okno przeglądarki Chromium.
> Zaloguj się swoim kontem Google, którego używasz na notebooklm.google.com.
> Po zalogowaniu wróć tutaj.

Uruchom:
```
python3 scripts/login.py
```

## KROK 6 — Zainstaluj skill Obsidian

Poinformuj użytkownika:
> Teraz zainstalujemy skill do Obsidian, który pozwoli agentowi bezpośrednio tworzyć i zarządzać notatkami w Twoim vault'cie.

Spróbuj najpierw przez Claude Code:
```
/plugin install obsidian@obsidian-skills
```

Jeśli komenda nie zadziała (błąd lub brak pluginu) — spróbuj przez npx (wymaga Node.js ≥ 18):
```
npx skills add git@github.com:kepano/obsidian-skills.git
```

Sprawdź czy Node.js jest zainstalowany przed uruchomieniem npx:
```
node --version
```

Jeśli brak Node.js — poinformuj użytkownika:
> Node.js możesz pobrać bezpłatnie ze strony nodejs.org (wersja LTS). Po instalacji wróć tutaj i wpisz `/setup` ponownie.

Po instalacji skilla poinformuj użytkownika:
> Skill Obsidian zainstalowany! Musisz teraz zrestartować Claude Code, aby skill został załadowany.
> 1. Wpisz `/exit`
> 2. Otwórz Claude Code ponownie w tym samym folderze
> 3. Wróć do konfiguracji — wpisz `/setup` (pozostałe kroki zostaną pominięte)

## Po zakończeniu wszystkich kroków

Poinformuj użytkownika że setup jest gotowy i zaproponuj `/research` aby zacząć budować pierwszą bazę wiedzy.
