numbers = input("Podaj liczby")
numbers = numbers.split(",")
print(numbers)
numbers_as_float = []
list_exc = []

for index, elem in enumerate(numbers):
    try:
        numbers[index] = float(elem)
    except ValueError as exc:  #mozna wiecej bledow naraz wrzucic, po przecinku
        list_exc.append(exc)
        numbers[index] = '-'

print(numbers)
while '-' in numbers:
    numbers.remove('-')
print(numbers)

avg = sum(numbers)/len(numbers)
print(avg)
print("lista bledow:", list_exc)

with open('bledy.txt', 'w') as f:
    f.write("ha mamy bledy! \n")
    for i in list_exc:
        f.write(str(i) + "\n")
