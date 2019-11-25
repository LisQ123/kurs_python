class Pojazdy:
    def __init__(self):
        print('Mozna mna jezdzic!')


class Samochod(Pojazdy):
    def opis(self):
        print('4 kolka, 4 miejsca')


class Rower(Pojazdy):
    def opis(self):
        print('2 kola, 1 miejsce')

class Autobus(Pojazdy):
    def opis(self):
        print('duzo kol i mnostwo miejsc!')

class Ciezarowka(Pojazdy):
    def opis(self):
        print('duzo kol i przyczepa!')

print(Ciezarowka())