  # zamiana stopni
przedmiot = 0
while przedmiot != 3:
    subject = input("przedmiot szkolny: ")
    grade = input("ocena w skali 1-6: ")
    print(subject + ": " + grade)
    przedmiot = przedmiot + 1

p = input("podaj przemioty podzielone myslnikiem: ")   # inny sposob
o = input("podaj oceny podzielone myslnikiem")

p = p.split("-")
o = o.split("-")

licznik = 0
while licznik < 3:
    print(p[licznik], "-", o[licznik])
    licznik = licznik + 1
