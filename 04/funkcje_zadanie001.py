  # 1. Napisz funkcje, ktora pyta uzytkownika o pary ksiazka + cena i zapisuje je w programie
  # 2. napisz funkcje ktora zapyta o ocene ksiazki i wyswietli ksiazke wraz
  #   z ocena jesli ksiazka o takiej ocenie istnieje.

def add_book(dict_books):
    counter = int(input("Ile ksiazek chcesz dodac? : "))
    for _ in range(counter):
        title = input("Podaj tytul ksiazki: ")
        grade = int(input("Podaj ocene: "))
        dict_books[title] = grade

    return dict_books

def read_book_by_grade(libr):
    g = input("Podaj ocene ksiazki jaka chcesz znalezc i przeczytac: ")
    if g in libr.values():
        for title, grade in libr.items():
            if grade == g:
                print(title, " - ocena:", grade)
    else:
        print("Nie ma ksiazki o takiej ocenie")

books = {}
books = add_book(books) # parametr przesylany do funkcji add_book()
read_book_by_grade(books)
print(books)




print("*" * 10)
