import random

def random_quote(words):
    quote_for_today = random.choice(words).strip()
    return  quote_for_today.split(' - ')

def show(quote):
    print("Twoj cytat na dzis to: ")
    print("*" * 100)
    print(quote[0].center(100))
    print((" ~" + quote[1]).center((100)))
    print("*" * 100)

cytat = "cytaty.txt"
with open(cytat, 'r', encoding='utf-8') as f:
    quotes = f.readlines()

for i in range(3):
    sentence = random_quote(quotes)
    print("^" * 20)
    show(sentence)
