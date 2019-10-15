weight = input("Podaj wagę w kg: ")
height = input("Podaj wzrost w metrach: ")

BMI = float(weight) / ( float(height) ** 2 )
print("Twoje BMI wynosi", BMI)

if BMI < 18.5:
    print("Niedowaga!")
elif BMI > 18.5 and BMI < 24.99:
    print("Waga prawidlowa!")
elif BMI >= 25.0:
    print("Nadwaga!")