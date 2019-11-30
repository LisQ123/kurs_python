# Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch
# znaków i zwracający ten sam tekst zmieniony na wielkie litery.
# Utwórz funkcję zwracającą tekst
#
# Utwórz dekorator przyjujący tę funkcję
#
# Wywołaj funkcję, by sprawdzić, że decorator działa

def uppercase_decorator(txt_func):
    def nasted():
        txt = txt_func()   #
        txt = txt.upper()  # => HELLO
        return txt
    return nasted


@uppercase_decorator
def say_hello():
    return 'hello'


@uppercase_decorator
def say_hi():
    return 'hihihi'


print(say_hello())
print(say_hi())

# uppercased_text = uppercase_decorator(say_hello)
# print(uppercased_text())
