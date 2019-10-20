  #Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.
x = int(input("Podaj liczbę."))
if x % 3 == 0:
    print("Twoja liczba jest podzielna przez 3.")
print("Koniec.")
