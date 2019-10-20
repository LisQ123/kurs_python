  # Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.
a = int(input("podaj liczbe: "))
b = int(input("podaj liczbe: "))
c = int(input("podaj liczbe: "))

if a > b > c:
    print(a, b, c)
elif b > a > c:
    print(b, a, c)
elif b > c > a:
    print(b, c, a)
elif c > a > b:
    print(c, a, b)
elif c > b > a:
    print(c, b, a)
