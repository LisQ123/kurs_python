names = input("Podaj imiona rozdzielone spacja: ")
names = names.split()
print(names)
for name in names:
    print("Hello ", name, "!")

print("___________")

id = 0
while id < len(names):
    print("Hi", names[id])
    id = id + 1
