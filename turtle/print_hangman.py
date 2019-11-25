import turtle


def print_hangman(t, incorrect):
    turtle.setup(1000, 600)
    screen = turtle.Screen()
    if incorrect == 1:
        t.pu()
        t.setx(-120)
        t.sety(180)
        t.pd()
        t.circle(20)
        t.ht()
    elif incorrect == 2:
        t.pu()
        t.setx(-100)
        t.sety(160)
        t.pd()
        t.fd(50)
        t.ht()
    elif incorrect == 3:
        t.rt(45)
        t.fd(30)
        t.ht()
    elif incorrect == 4:
        t.pu()
        t.rt(-90)
        t.setx(-100)
        t.sety(110)
        t.pd()
        t.fd(30)
        t.ht()
    elif incorrect == 5:
        t.pu()
        t.rt(-45)
        t.setx(-100)
        t.sety(135)
        t.pd()
        t.fd(30)
        t.ht()
    elif incorrect == 6:
        t.pu()
        t.rt(180)
        t.setx(-100)
        t.sety(135)
        t.pd()
        t.fd(30)
        t.pu()
        t.ht()


def rysu(t):
    t.pu()
    t.rt(180)
    t.setx(-100)
    t.sety(135)
    t.pd()
    t.fd(30)
    t.pu()
    t.ht()


print(rysu(6))