print("zad.2")
s1 = "mysz"
s2 = "kot"
print(s1[0:2:] + s2 + s1[2:4:])

print("zad.4")

name = input("Hello! What's your name? ")
titlee = input("Tell me the name of your favorite book, please! ")
author = input("Who does write this book? ")
pages = input("How many pages has this book? ")

print("Czy nazwisko składa się tylko z liter?", author.isalpha())
print("Czy nazwa książki składa się tylko z liter?", titlee.isalpha())
print("Czy liczba stron jest wartością liczbową?", pages.isnumeric())

print(name.capitalize())   #czy da sie zrobic by duze litery poprawialo juz na etapie input?
print(titlee.capitalize())
print(author.title())

book = name + " " + titlee + " " + author + " " + pages
print(book)
print(len(book))