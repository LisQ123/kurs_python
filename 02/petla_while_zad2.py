  # prosta gra, zgaduj liczbe
secret_num = 7
number = int(input("Let's play a game! Give me number 1-20: "))

while number != secret_num:
        print("Lose!")  #
        number = int(input("Give me another number 1-20:"))
print("Win!")
