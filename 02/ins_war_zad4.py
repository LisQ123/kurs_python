  # Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.
txt = "asdaaa"
if len(txt) > 5 and txt.count("a"):
    print(txt.replace("a", "z"))
