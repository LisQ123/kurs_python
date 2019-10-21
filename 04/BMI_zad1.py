  #kalk. BMI


def calc_bmi(weight, height):
    return weight / height ** 2


def bmi_status(bmi):
    if BMI < 18.5:
        print("Niedowaga!")
    elif BMI > 18.5 and BMI < 24.99:
        print("Waga prawidlowa!")
    elif BMI >= 25.0:
        print("Nadwaga!")

w = float(input("Podaj wagę w kg: "))
h = float(input("Podaj wzrost w metrach: "))
BMI = calc_bmi(w, h)
print("Twoje BMI wynosi: ", BMI)
status = bmi_status(BMI)
