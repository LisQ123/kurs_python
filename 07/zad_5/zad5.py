import pola_figur as pola
amount = int(input("How many rooms do you want?"))
room = input("choose the shape of the room: rectangle, trangle, square, diamond, trapeze.: ")
x = 0
while amount > x:
    if room == "rectangle":
        a = input("Give me first value")
        b = input("Give me second value")
        print(pola.rectangle_field(a, b))
        x = x + 1
    elif room == "square":
        a = input("Give me first value")
        print(pola.square_field(a))
        x = x + 1
    elif room == "diamond":
        a = input("Give me first value")
        b = input("Give me second value")
        print(pola.diamond_field(a, b))
        x = x + 1
    elif room == "trapeze":
        a = input("Give me first value")
        b = input("Give me second value")
        print(pola.trapeze_field(a, b))
        x = x + 1
    elif room == "trangle":
        a = input("Give me first value")
        b = input("Give me second value")
        print(pola.trangle_field(a, b))
        x = x + 1

