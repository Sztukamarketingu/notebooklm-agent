Przeprowadź pełny workflow badawczy: od tematu do gotowej bazy wiedzy w NotebookLM.

## Instrukcja krok po kroku

### 1. Ustal temat

Zapytaj użytkownika:
> Czego będziemy szukać? Możesz podać:
> - Temat ogólny (np. "marketing w social media", "strategie sprzedaży")
> - Konkretnych twórców (np. "Neil Patel", "Gary Vaynerchuk")
> - Kombinację (np. "Facebook Ads od ekspertów")

### 2. Ustal parametry

Zapytaj:
- Język wideo: **polski** czy **angielski**? (domyślnie: angielski dla większości tematów biznesowych)
- Ile wideo maksymalnie? (domyślnie: 10)
- Czy masz już notatnik w NotebookLM do którego chcesz dodać? (tak/nie)

### 3. Wyszukaj wideo

```
python3 scripts/youtube_search.py --topic "$TOPIC" --lang "$LANG" --max "$MAX" --min-views 5000
```

Pokaż wyniki. Zapytaj czy są OK, czy chce wykluczyć jakieś.

### 4. Stwórz lub wybierz notatnik

Jeśli nowy:
```
python3 scripts/create_notebook.py --title "$TOPIC – $(date +%Y-%m-%d)" --description "Baza wiedzy: $TOPIC"
```

### 5. Dodaj wideo

```
python3 scripts/add_to_notebook.py --notebook-id "$NOTEBOOK_ID" --urls "$URLS"
```

Pokazuj postęp dla każdego wideo.

### 6. Podsumowanie

Po zakończeniu pokaż:
- Nazwa notatnika
- Ile wideo dodano
- Link: https://notebooklm.google.com

Oraz zasugeruj przykładowe pytania które użytkownik może zadać w NotebookLM, dopasowane do tematu. Na przykład dla marketingu:
- "Jakie są najskuteczniejsze strategie pozyskiwania klientów w 2024?"
- "Porównaj podejście do content marketingu z różnych materiałów"
- "Jakie błędy w reklamach Facebook najczęściej popełniają małe firmy?"
