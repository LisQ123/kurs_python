# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.


filename = "karty_kredytowe.txt"

with open(filename, 'w+') as f:
    card_number = f.readline()


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


can_be_card_number = False
if len(card_number) < 13 or len(card_number) > 16:
    print("Wrong number")
else:
    if card_number.isdecimal():
        print("Can be card number")
        can_be_card_number = True
    else:
        print("Not a number")


if is_visa(can_be_card_number, card_number):
    print("Visa!")
elif is_mastercard(can_be_card_number, card_number):
    print("Mastercard!")
elif is_american_express(can_be_card_number, card_number):
    print("American Express!")
else:
    print("Not known card number.")
