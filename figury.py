def triangle_field(base, height):
    result = 0.5 * base * height
    return result


def square_field(base):
    result = base ** 2
    return result


def diamond_field(base, height):
    result = base * height
    return result


def trapeze_field(base, side, height):
    result = ((base + side) * height)/2
    return result


print("Modul zaimportowany")
