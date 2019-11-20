import turtle

spin = turtle.Turtle()
roller = turtle.Screen()
roller.bgcolor("black")
spin.pensize(5)
spin.speed(200)
spin.pencolor("yellow")


def Spinner(spin, match):
    spin.fd(match)
    spin.rt(60)
    Spinner(spin, match - 4)


Spinner(spin, 200)
mainloop()
