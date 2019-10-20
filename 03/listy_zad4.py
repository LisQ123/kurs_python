# pobierz parzysta liczbe elementow. czy srodkowe sa takie same?
wielkosc = int(input("Podaj z ilu elementow bedzie sie skladac Twoj zbior, niech bedzie to parzysta liczba: "))
while wielkosc%2 == 1:
    wielkosc =int(input("Podaj parzysta liczbe!: "))

zbior = []
for i in range(wielkosc):
    elements = input("Podaj element: ")
    zbior.append(elements)
sr = int(len(zbior)/2)
sr1 = zbior[sr]
sr2 = zbior[sr - 1]

if sr1 == sr2:
    print("Srodkowe elementy sa takie same")
else:
    print("Srodkowe elementy sa rozne")
