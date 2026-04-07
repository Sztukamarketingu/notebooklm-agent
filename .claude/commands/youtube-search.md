Wyszukaj wideo na YouTube na podany temat i pokaż wyniki użytkownikowi.

## Instrukcja

1. Jeśli użytkownik nie podał tematu — zapytaj: "Na jaki temat mam wyszukać wideo?"

2. Zapytaj o filtry (jeśli użytkownik nie podał):
   - Język: polski czy angielski?
   - Ile wyników? (domyślnie 10)
   - Minimalna liczba wyświetleń? (domyślnie 1000)

3. Uruchom wyszukiwanie:
```
python3 scripts/youtube_search.py --topic "$TOPIC" --lang "$LANG" --max "$MAX" --min-views "$MIN_VIEWS"
```

4. Pokaż wyniki w czytelnej formie: tytuł, kanał, liczba wyświetleń, czas trwania, link.

5. Zapytaj użytkownika:
   - "Czy chcesz dodać te wideo do notatnika NotebookLM?"
   - Jeśli tak — zaproponuj `/create-notebook` lub `/add-to-notebook` (jeśli notatnik już istnieje)

## Przykłady tematów

Gdy użytkownik pyta o pomysły:
- "marketing w mediach społecznościowych 2024"
- "jak pisać skuteczne reklamy Facebook"  
- "strategia content marketingu"
- "Google Ads dla początkujących"
