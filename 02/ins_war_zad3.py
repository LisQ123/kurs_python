  #Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.
a = int(input("Podaj pierwsza opinie od 1 do 10: "))
b = int(input("Podaj druga opinie od 1 do 10: "))
c = int(input("Podaj trzecia opinie od 1 do 10: "))
sr = (a + b + c) / 3
if sr > 7:
    print("bdb")
elif sr <= 7 and sr >= 5:
    print("dst")
elif sr <= 4:
    print("nd")