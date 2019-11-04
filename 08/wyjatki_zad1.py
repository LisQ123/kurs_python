def dzielenie(x):
    result = x / 10
    return result

wyjatkowa_lista = [0, 13, 'xd', 12.3, True, ["a", "b"], {1, 2, 3}, 4+3, {"pl":"poland"}]

for i in wyjatkowa_lista:
    try:
        result = 10 / i
    except ZeroDivisionError as e:
        result = "wyjatek 1: ", str(e)
    except TypeError as e:
        result = "wyjatek 2: ", str(e)

    print(result)
