import sys

def hello_exception():
try:
    hello_exception()
except ArithmeticError as ex:
    print("oh nie blad", ex)

    print(sys.exc_info())

except:
    print("inny blad")
