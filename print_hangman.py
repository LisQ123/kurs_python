
# print('        ┌--------┐')
# print('        |        |')
# print('        |        O')
# print('        |       -┼-')
# print('        |       ┌┴┐')
# print('     ___|___ ')


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def draw(points):
    if points == 1:
        print('     ___|___ ')

    elif points == 2:
        print('        |       ')
        print('     ___|___ ')
    elif points == 3:
        print('        ┌')
        print('        |        ')
        print('        |        ')
        print('        |       ')
        print('        |       ')
        print('     ___|___ ')
    elif points == 4:
        print('        ┌--------')
        print('        |        ')
        print('        |        ')
        print('        |       ')
        print('        |       ')
        print('     ___|___ ')
    elif points == 5:
        print('        ┌--------┐')
        print('        |        |')
        print('        |        ')
        print('        |       ')
        print('        |       ')
        print('     ___|___ ')
    elif points == 6:
        print('        ┌--------┐')
        print('        |        |')
        print('        |        O')
        print('        |       ')
        print('        |       ')
        print('     ___|___ ')
    elif points == 7:
        print('        ┌--------┐')
        print('        |        |')
        print('        |        O')
        print('        |       -┼-')
        print('        |       ')
        print('     ___|___ ')
    elif points == 8:
        print('        ┌--------┐')
        print('        |        |')
        print('        |        O')
        print('        |       -┼-')
        print('        |       ┌┴')
        print('     ___|___ ')
    elif points == 9:
        print(prRed('        ┌--------┐'))
        print(prRed('        |        |'))
        print(prRed('        |        O'))
        print(prRed('        |       -┼-'))
        print(prRed('        |       ┌┴┐'))
        print(prRed('     ___|___  YOU ARE DEAD!'))

draw(9)