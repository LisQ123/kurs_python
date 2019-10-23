# if len(card) < 13 and first value = 4 --> visa
# if len(card) = 16 and 51 < first values < 55, else 2221 < first values < 2720 --> mastercard
# if len(card) = 15 and first value = 34 else 37 --> american

# mastercard = 5379018074707179
# visa = 4127142102277951
# american = 373937499286823


def is_visa(is_card, number):
    if not is_card:
        return False

    if can_be_card_number and (len(number) == 16 or len(number) == 13):
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


card_number = input("Put your card number here: ")
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
