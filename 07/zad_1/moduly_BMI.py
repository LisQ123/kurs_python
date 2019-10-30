def calc_bmi(weight, height):
    return weight / height ** 2


def bmi_status(bmi):
    if bmi < 18.5:
        return "Niedowaga!"
    elif bmi > 18.5 and bmi < 24.99:
        return "Waga prawidlowa!"
    elif bmi >= 25.0:
        return "Nadwaga!"


def main():
    BMI = calc_bmi(63, 1.73)
    status = bmi_status(BMI)
    print("Twoje BMI wynosi: ", BMI, status)


if __name__ == '__main__':
    main()
