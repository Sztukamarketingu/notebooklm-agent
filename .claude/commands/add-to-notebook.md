Dodaj wideo z YouTube do istniejącego notatnika NotebookLM.

## Instrukcja

1. Sprawdź czy użytkownik ma już notatnik. Przejrzyj `config/settings.yaml` — pole `notebook.id`.

2. Jeśli brak notatnika — zaproponuj najpierw `/create-notebook`.

3. Jeśli użytkownik podał URL bezpośrednio — dodaj go:
```
python3 scripts/add_to_notebook.py --notebook-id "$NOTEBOOK_ID" --urls "$URL"
```

4. Jeśli chce wyszukać nowe wideo — wykonaj wyszukiwanie (jak w `/youtube-search`), pokaż wyniki, zapytaj które dodać.

5. Przy dodawaniu informuj na bieżąco:
   - [1/10] Dodano: "Tytuł wideo" – Kanał
   - [2/10] Pominięto: "Tytuł" – brak transkryptu

6. Na koniec podsumuj: ile dodano, ile pominięto, dlaczego.

## Limity NotebookLM

- Max 50 źródeł na notatnik
- Jeśli limit osiągnięty — zaproponuj stworzenie nowego notatnika
