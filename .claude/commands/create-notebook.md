Stwórz nowy notatnik w NotebookLM i opcjonalnie dodaj do niego wideo z YouTube.

## Instrukcja

1. Zapytaj o temat notatnika jeśli nie podano:
   "Jak ma się nazywać notatnik i czego dotyczy? (np. 'Marketing 2024 – strategie social media')"

2. Stwórz notatnik:
```
python3 scripts/create_notebook.py --title "$TITLE" --description "$DESCRIPTION"
```

3. Wyświetl wynik: nazwa notatnika, ID, link do NotebookLM.

4. Zapytaj: "Czy chcesz teraz wyszukać wideo YouTube i dodać je do notatnika?"

5. Jeśli tak:
   a. Wyszukaj wideo (patrz logika z `/youtube-search`)
   b. Dodaj do notatnika:
   ```
   python3 scripts/add_to_notebook.py --notebook-id "$NOTEBOOK_ID" --urls "$URLS"
   ```

6. Po dodaniu poinformuj:
   > NotebookLM przetwarza teraz transkrypty wideo. Może to potrwać kilka minut.
   > Gdy skończy — otwórz notebooklm.google.com i możesz zadawać pytania swojej bazie wiedzy!

## Przykładowe opisy notatników

- "Baza wiedzy: strategie marketingowe z YouTube 2024"
- "Notatnik sprzedażowy: techniki B2B od ekspertów"
- "Kursy online: Python i machine learning"
