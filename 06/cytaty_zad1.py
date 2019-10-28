import random
cytat = input("Podaj nazwe pliku z cytatami: ")
with open(cytat, 'r', encoding='utf-8') as f:
    quotes = f.readlines()

quote_for_today = random.choice(quotes).strip()
quote_for_today = quote_for_today.split(' - ')
print(quote_for_today)

print("Twoj cytat na dzis to: ")
print("*" * 100)
print(quote_for_today[0].center(100))
print((" ~" + quote_for_today[1]).center((100)))
print("*" * 100)
