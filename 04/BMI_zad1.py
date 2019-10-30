  #kalk. BMI


def calc_bmi(weight, height):
    return weight / height ** 2


def bmi_status(bmi):
    if BMI < 18.5:
        return "Niedowaga!"
    elif BMI > 18.5 and BMI < 24.99:
        return "Waga prawidlowa!"
    elif BMI >= 25.0:
        return "Nadwaga!"


w = float(input("Podaj wagę w kg: "))
h = float(input("Podaj wzrost w metrach: "))
BMI = calc_bmi(w, h)
status = bmi_status(BMI)
print("Twoje BMI wynosi: ", BMI, status)

