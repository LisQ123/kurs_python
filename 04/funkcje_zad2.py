  # Napisać funkcję, która sprawdza czy liczba jest parzysta.

def czy_parzysta(liczba):
    if int(liczba) % 2:
        print("Twoja liczba nie jest parzysta!")
    else:
        print("Twoja liczba jest parzysta!")
    return


podana_liczba = input("Podaj liczbe, sprawdzimy czy jest parzysta ;) :")
czy_parzysta(podana_liczba)
