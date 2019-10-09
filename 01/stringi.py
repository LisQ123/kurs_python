nr = "123887"
print(nr.isdecimal())
nienr = "asd123"
print(nienr.isdecimal())

text = "looLoo"
print(text.isalpha() and not text.islower())

txt = "banana"
print(txt.count("na"))

print ("Zadania nieparzyste")
print ("Zad.1")
wyraz = "ciastko"
print (wyraz[2:5:])
print (len(wyraz))  # sposób z len()
middle = len(wyraz) / 2
middle = len(wyraz) // 2
print (wyraz[middle - 1] + wyraz[middle] + wyraz[middle + 1])

print ("Zad.3")
quote = "Honesty is the first chapter in the book of wisdom."
print (len(quote))  # 1
print (quote[44:50:])  # 2 pokombinuj potem sprytniej
print (quote[-7:-1:])
print (quote[0:25])  # 3
print (quote[-1])  # 4
print (quote[len(quote) // 2:: 3])  # 5
print (quote[:: 2])  # 6
print (quote)  # dokoncz

print("Zad. 5")
txt = "kajak"
print(txt)
print(txt[::-1])
print(txt == txt[::-1])
zdanie = "kobyla ma maly bok"
print(zdanie)
zdanie.replace(" ", "")
zdanie = zdanie.replace(" ", "")
print(zdanie[::-1])
print(zdanie == zdanie[::-1] )
