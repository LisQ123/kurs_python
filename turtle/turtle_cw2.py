import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
skk=turtle.Turtle()
skk.color("blue")


def func(size):
    for i in range(40):
        skk.fd(size)
        skk.left(90)
        size = size + 5


func(6)
func(26)
func(36)
func(46)