  # def max_func(a, b, c):  # Nie korzystając z funkcji wbudowanej max(),
  # napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_func(a, b, c):
    if a <= b:
        if c <= a:
            print('Max: ', b)
        else:
            if b <= c:
                print('Max: ', c)
            else:
                print('Max:', b)
    else:
        if c <= b:
            print('Max: ', a)
        else:
            if c <= a:
                print('Max: ', a),
            else:
                print('Max: ', c)


a = float(input('Podaj liczbe a: '))
b = float(input('Podaj liczbe b: '))
c = float(input('Podaj liczbe c: '))