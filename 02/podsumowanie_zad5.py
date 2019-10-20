 #gra cieplo zimno
import random
numbers = random.randint(1, 100)


for i in range(6):
    traf = int(input("wpisz dowolna liczbe od 1 do 100:  "))
    if numbers == traf:
        print("Winner!")
        break
    else:
        print("Try again!")

    if traf > numbers:
        print("Your number is too high!")
    elif traf < numbers:
        print("Your number is too low!")
