# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

filename = "karty_kredytowe.txt"


def is_visa(is_card, number):
    if not is_card:
        return False

    if len(number) == 16 or len(number) == 13:
        if number[0] == "4":
            return True


def is_mastercard(is_card, number):
    if not is_card:
        return False

    if len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True


def is_american_express(is_card, number):
    if not is_card:
        return False

    if len(number) == 15:
        if number[0:2] in ("34", "37"):
            return True

with open(filename, 'r') as f:
    card_number = f.readline()

cards = []

for i in card_number:
    cards.append(card_number.strip())
print(cards)


for card_number in cards:
    can_be_card_number = False
    if len(card_number) < 13 or len(card_number) > 16:
        print("Wrong number")
    else:
        if card_number.isdecimal():
            print("Can be card number")
            can_be_card_number = True
        else:
            print("Not a number")


for card_number in cards:
    if is_visa(can_be_card_number, card_number):
        print(card_number, 'visa')
        with open('visa.txt', 'a') as f:
            f.write(f'\n{card_number}')
    if is_mastercard(can_be_card_number, card_number):
        print(card_number, 'mastercard')
        with open('mastercard.txt', 'a') as f:
            f.write(f'\n{card_number}')
    if is_american_express(can_be_card_number, card_number):
        print(card_number, 'americanexpress')
        with open('americanexpress.txt', 'a') as f:
            f.write(f'\n{card_number}')
