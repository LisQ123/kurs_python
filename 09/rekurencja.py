def suma_for(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print('Suma - for: ', suma_for(10))


def suma_while(n):
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s


print('suma while: ', suma_while(10))


def sum_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursion(n-1)


print('suma reku: ', sum_recursion(10))