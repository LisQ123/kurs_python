filename = 'tekst.txt'

with open('tekst.txt', 'r', encoding='utf-8') as fopen:
    list_of_lines = fopen.readlines()


print(list_of_lines)
print("---------------")


for i in range(4):
    print(f"Line {i}: " + list_of_lines[i].strip(), end="***")
