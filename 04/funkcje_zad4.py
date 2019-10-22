def czy_parzysta(lista_liczb):
    parzyste = []
    nieparzyste = []
    for liczba in lista_liczb:
        if liczba % 2 ==0:
                parzyste.append(liczba)
        else:
                nieparzyste.append(liczba)
    return parzyste



podana_liczba = {input("Podaj liczby. Sprawdzimy, ktore sa parzyste : ")}
czy_parzysta(podana_liczba)
