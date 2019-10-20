  #Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
a = int(input("Podaj liczbe"))
b = int(input("podaj kolejna liczbe"))
wynik = a + b
if wynik > 100:
    print(wynik)
else:
    print("Koniec")