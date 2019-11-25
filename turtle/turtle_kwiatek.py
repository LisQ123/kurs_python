import turtle


def kwiatek(i):
    turtle.color()
    turtle.pensize(3)
    for i in range(36):
        turtle.forward(100)
        turtle.left(110)


kwiatek(8)
turtle.mainloop()