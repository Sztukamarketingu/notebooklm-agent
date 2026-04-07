Eksportuj wyniki badań do Obsidian i zbuduj długoterminową bazę wiedzy.

## Co robi ta komenda

Każda sesja badawcza tworzy w Obsidian:
- Notatkę dla każdego wideo (tytuł, kanał, link, kluczowe wnioski)
- MOC (Map of Content) dla całego tematu — widok z lotu ptaka
- Tagi umożliwiające filtrowanie po tematach i twórcach
- Linki [[wiki-links]] między powiązanymi tematami

Z czasem vault staje się osobistą bazą wiedzy z grafem powiązań.

## Instrukcja

### 1. Ustal ścieżkę do vault'u

Jeśli użytkownik nie podał ścieżki — zapytaj:
> "Gdzie jest Twój vault Obsidian? Podaj ścieżkę do folderu, np. `/Users/imie/Documents/MyVault`"

Jeśli nie ma Obsidian — powiedz:
> "Obsidian możesz pobrać bezpłatnie ze strony obsidian.md. Po zainstalowaniu utwórz nowy vault i podaj mi jego ścieżkę."

Zapisz ścieżkę w `config/settings.yaml` pod kluczem `obsidian.vault_path` — żeby nie pytać za każdym razem.

### 2. Uruchom eksport

```
python3 scripts/obsidian_export.py --vault-path "$VAULT_PATH" --topic "$TOPIC"
```

### 3. Tryb nauki (opcjonalny)

Zapytaj:
> "Czy chcesz stworzyć karty do nauki (flashcards) z tych materiałów?"

Jeśli tak — uruchom z flagą:
```
python3 scripts/obsidian_export.py --vault-path "$VAULT_PATH" --topic "$TOPIC" --flashcards
```

Flashcards tworzą plik `_Flashcards.md` z pytaniami i odpowiedziami na podstawie materiałów, gotowy do użycia z pluginem Spaced Repetition.

### 4. Pokaż wynik

Po eksporcie poinformuj:
- Ile notatek utworzono/zaktualizowano
- Gdzie w vault się znajdują (np. `NotebookLM/marketing/`)
- Że użytkownik może otworzyć Obsidian i zobaczyć graf powiązań (Ctrl/Cmd + G)

## Struktura notatek w vault

```
vault/
└── NotebookLM/
    └── [temat]/
        ├── _MOC.md            ← mapa tematu z linkami do wszystkich wideo
        ├── _Flashcards.md     ← karty do nauki (opcjonalne)
        └── [Tytuł wideo].md   ← notatka dla każdego wideo
```

## Format notatki wideo

Każda notatka zawiera:
```markdown
# [Tytuł wideo]

## Metadane
- **Kanał:** [nazwa]
- **Link:** [URL]
- **Wyświetlenia:** [liczba]
- **Dodano:** [data]

## Kluczowe wnioski
[do uzupełnienia przez użytkownika lub AI]

## Cytaty i notatki
[miejsce na własne notatki]

## Powiązane tematy
[[inne-tematy]]

#notebooklm #[temat] #[kanał]
```
