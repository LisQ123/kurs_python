def calc_bmi(weight, height):
    return weight / height ** 2


def bmi_status(BMI):
    if BMI < 18.5:
        return "Niedowaga!"
    elif BMI > 18.5 and BMI < 24.99:
        return "Waga prawidlowa!"
    elif BMI >= 25.0:
        return "Nadwaga!"


try:
    w = float(input("Podaj wagę w kg: "))
    h = float(input("Podaj wzrost w metrach: "))
    bmi = calc_bmi(w, h)
    status = bmi_status(bmi)
    print("Twoje BMI wynosi: ", bmi, status)
except ValueError as e:
    print("Podaj parametry w formacie liczbowym!")

