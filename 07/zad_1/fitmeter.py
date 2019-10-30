import moduly_BMI as b

def advice(filename):
    with open(filename + ".txt") as f:
        content = f.read()

    print(content)


def main():
    w = float(input("Podaj wagę w kg: "))
    h = float(input("Podaj wzrost w metrach: "))
    bmi_result = b.calc_bmi(w, h)
    bmi_stan = b.bmi_status(bmi_result)
    print(bmi_stan)
    advice((bmi_stan))

if __name__ == '__main__':
    main()

