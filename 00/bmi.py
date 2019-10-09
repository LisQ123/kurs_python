weight = input("Podaj wagę w kg: ")
height = input("Podaj wzrost w metrach: ")

BMI = float(weight) / ( float(height) ** 2 )  #udalo sie wykombinowac
print("Twoje BMI wynosi", BMI)