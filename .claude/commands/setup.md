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

## KROK 6 — Zainstaluj skill NotebookLM

Poinformuj użytkownika:
> Teraz zainstalujemy skill, który daje Claude Code bezpośredni dostęp do NotebookLM.

Spróbuj najpierw przez wbudowaną komendę:
```
notebooklm skill install
```

Jeśli nie zadziała — przez npx (wymaga Node.js ≥ 18):
```
npx skills add teng-lin/notebooklm-py
```

Weryfikacja:
```
notebooklm skill list
```

Jeśli skill widoczny na liście — przejdź dalej.

## KROK 7 — Zainstaluj skill Obsidian

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

Po instalacji obu skilli poinformuj użytkownika:
> Oba skille zainstalowane! Musisz teraz zrestartować Claude Code, aby zostały załadowane.
> 1. Wpisz `/exit`
> 2. Otwórz Claude Code ponownie w tym samym folderze
> 3. Wróć do konfiguracji — wpisz `/setup` (już wykonane kroki zostaną pominięte)

## KROK 8 — Zainstaluj komendy globalnie

Poinformuj użytkownika:
> Ostatni krok! Skopiuję komendy agenta do globalnego folderu Claude Code — dzięki temu będziesz mógł używać `/research`, `/compare` i pozostałych komend z **dowolnego folderu**, nie tylko z tego projektu.

Uruchom:
```
python3 scripts/install_global.py
```

Jeśli się powiedzie — poinformuj:
> Komendy zainstalowane globalnie! Od teraz możesz otworzyć Claude Code gdziekolwiek i wpisać `/research` — agent zawsze będzie dostępny.

Jeśli błąd — powiedz użytkownikowi że komendy działają lokalnie (w tym folderze) i można wrócić do tego kroku później.

## Po zakończeniu wszystkich kroków

Podsumuj co zostało zainstalowane:
- Python + biblioteki (notebooklm-py, youtube-search-python)
- Przeglądarka Chromium (logowanie do NotebookLM)
- Skill NotebookLM — globalny
- Skill Obsidian — globalny
- Komendy agenta — globalne (dostępne wszędzie)

Następnie zaproponuj pierwszą sesję:
> Wszystko gotowe! Wpisz `/research` żeby zbudować pierwszą bazę wiedzy — możesz to zrobić teraz lub w dowolnym momencie, z dowolnego folderu.
