import gry
import random


print("Witaj w najprostszej grze na swiecie!\n")
again = None
while again != "n":
    players = []
    num = gry.ask_number(question="Podaj liczbę graczy (2 - 5): ", low=2, high=5)
    for i in range(num):
        name = input("Nazwa gracza: ")
        score = random.randrange(100) + 1
        player = gry.Player(name, score)
        players.append(player)

    print("\nOto wyniki gry:")
    for player in players:
        print(player)

    again = gry.ask_yes_no("\nCzy chcesz zagrac ponownie? (t/n): ")

input("\n\nAby zakonczyc program, nacisnij klawisz Enter.")
