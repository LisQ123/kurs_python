def predict_future():
    num = int(input("Podaj dowolna liczbe naturalna:  "))
    if num < 0:
        raise ValueError("To nie jest liczba naturalna!")
    else:
        print("Za", 10 * num, "ludzkosc bedzie mogla sie teleportowac")


try:
    predict_future()
except ValueError as e:
    print("*")
    print(e)
