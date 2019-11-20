import turtle

def square(lenght):
    for i in range(4):
        turtle.forward(lenght)
        turtle.left(90)
    return


count = 0
while count < 90:
    square(90)
    turtle.right(4)
    count += 1

turtle.exitonclick()