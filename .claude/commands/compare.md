Zbierz materiały od dwóch twórców/kanałów na ten sam temat i zbuduj notatnik do analizy porównawczej — burzy mózgów i dyskusji perspektyw.

## Instrukcja

### 1. Ustal temat i dwóch twórców

Jeśli użytkownik nie podał — zapytaj:
> Na jaki temat chcesz porównać perspektywy?
> Podaj dwóch twórców, kanały lub ekspertów (np. "Neil Patel" i "Gary Vaynerchuk")

Zapisz jako: TOPIC, CREATOR_A, CREATOR_B

### 2. Wyszukaj wideo od każdego osobno

```
python3 scripts/youtube_search.py --topic "$TOPIC $CREATOR_A" --max 5 --min-views 1000
```
```
python3 scripts/youtube_search.py --topic "$TOPIC $CREATOR_B" --max 5 --min-views 1000
```

Pokaż wyniki dla każdego twórcy osobno z nagłówkami:
> **[Creator A] — 5 wideo**
> 1. "Tytuł" — X wyświetleń
> ...
>
> **[Creator B] — 5 wideo**
> 1. "Tytuł" — X wyświetleń
> ...

Zapytaj czy lista wygląda OK, czy chce coś zmienić.

### 3. Stwórz notatnik porównawczy

```
python3 scripts/create_notebook.py \
  --title "$CREATOR_A vs $CREATOR_B: $TOPIC" \
  --description "Analiza porównawcza perspektyw: $CREATOR_A kontra $CREATOR_B na temat: $TOPIC"
```

### 4. Dodaj wideo obu twórców do jednego notatnika

Najpierw wideo Creator A, potem Creator B:
```
python3 scripts/add_to_notebook.py --notebook-id "$NOTEBOOK_ID" --urls "$URLS_A"
python3 scripts/add_to_notebook.py --notebook-id "$NOTEBOOK_ID" --urls "$URLS_B"
```

Pokazuj postęp z oznaczeniem kto jest autorem każdego wideo.

### 5. Wygeneruj pytania do debaty

Po zakończeniu pokaż gotowe pytania do wklejenia w NotebookLM, dopasowane do tematu i twórców. Przykłady dla marketingu:

**Pytania porównawcze:**
- „Jak $CREATOR_A i $CREATOR_B różnią się w podejściu do [tematu]? Kto ma rację?"
- „Jakie strategie poleca $CREATOR_A, których $CREATOR_B by unikał?"
- „W czym obaj twórcy się zgadzają mimo różnych stylów?"

**Pytania z perspektywy jednego twórcy:**
- „Jak $CREATOR_A rozwiązałby problem X? Podaj konkretne kroki."
- „Co $CREATOR_B powiedziałby na temat strategii Y? Czy by ją polecił?"

**Pytania do burzy mózgów:**
- „Gdyby $CREATOR_A i $CREATOR_B mieli razem doradzić firmie Z, na co by się zgodzili, a gdzie by się kłócili?"
- „Połącz najlepsze rady obu twórców w jeden plan działania."

### 6. Obsidian (opcjonalnie)

Jeśli użytkownik ma Obsidian — stwórz dodatkową notatkę porównawczą:

```
python3 scripts/obsidian_export.py --vault-path "$VAULT_PATH" \
  --topic "$CREATOR_A vs $CREATOR_B - $TOPIC"
```

Notatka `_MOC.md` powinna zawierać sekcje:
- **Perspektywa $CREATOR_A** — linki do jego wideo
- **Perspektywa $CREATOR_B** — linki do jego wideo
- **Punkty sporu** — miejsce na własne notatki
- **Punkty zgody** — miejsce na własne notatki
- **Mój wniosek** — miejsce na decyzję użytkownika
