  #maximum_of(a, b, c)


def max_of_2(first, second):
    return first if first > second else second


def maximum_of(a, b, c):
    return max_of_2(max_of_2(a, b), c)


def read_value():
    return int(input("Put integer value :"))


x = read_value()
y = read_value()
z = read_value()

result = maximum_of(x, y, z)
print("Max of: ", x, y, z, " is", result)
