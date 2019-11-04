w = float(input("podaj wage"))
h = float(input("podaj wzrost"))

bmi = "nie zdefiniowano"
try:
    bmi = w / h ** 2
except ZeroDivisionError as e:
    print("Wzrost ni emoze byc zerem")
    bmi = 0

print("twoje bmi:", bmi)
