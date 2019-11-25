import random
# import print_hangman as rysu  # z jakiegos powodu importy mi nie dzialaja


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def draw(points):
    if points == 1:
        print('     ___|___ ')

    elif points == 2:
        print('        |       ')
        print('     ___|___ ')
    elif points == 3:
        print('        ┌')
        print('        |        ')
        print('        |        ')
        print('        |       ')
        print('        |       ')
        print('     ___|___ ')
    elif points == 4:
        print('        ┌--------')
        print('        |        ')
        print('        |        ')
        print('        |       ')
        print('        |       ')
        print('     ___|___ ')
    elif points == 5:
        print('        ┌--------┐')
        print('        |        |')
        print('        |        ')
        print('        |       ')
        print('        |       ')
        print('     ___|___ ')
    elif points == 6:
        print('        ┌--------┐')
        print('        |        |')
        print('        |        O')
        print('        |       ')
        print('        |       ')
        print('     ___|___ ')
    elif points == 7:
        print('        ┌--------┐')
        print('        |        |')
        print('        |        O')
        print('        |       -┼-')
        print('        |       ')
        print('     ___|___ ')
    elif points == 8:
        print('        ┌--------┐')
        print('        |        |')
        print('        |        O')
        print('        |       -┼-')
        print('        |       ┌┴')
        print('     ___|___ ')
    elif points == 9:
        print(prRed('        ┌--------┐'))
        print(prRed('        |        |'))
        print(prRed('        |        O'))
        print(prRed('        |       -┼-'))
        print(prRed('        |       ┌┴┐'))
        print(prRed('     ___|___  YOU ARE DEAD!'))


def word_choice():  # losowanie slowa z pliku
    words = []
    with open('hasla.txt', 'r') as fopen:
        all_words = fopen.readlines()
        words.append(all_words)
        for i in words:
            chosen_word = random.choice(i)
    return chosen_word


def play_again():
    question = input('Do you want to play again? yes/no ')
    draw(9)
    if question.lower() == 'yes':
        hangman()
    else:
        exit()


def hangman():
    print('Welcome to hangman game')
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    guessed_letters = []   # lista uzytych liter
    word = word_choice()
    hidden_word = []
    for letter in word:
        hidden_word.append('_')  # ukryte litery
    check = False
    game_round = 1
    while game_round < 9 and not check:
        print('*' * 10)
        print('Word to guess: ', ' '.join(hidden_word))
        print('Letters to use: ', alphabet)
        print('Used letters: ', guessed_letters)
        user_letter = input('Give me a letter, to quit write - exit ')
        draw(game_round)
        for i in alphabet:
            if user_letter == i:
                alphabet.remove(i)
        for i in guessed_letters:
            if user_letter == i:
                print('You have already guessed that letter!')
                game_round += 1
                check = True
                continue  # nie idzie dalej
        guessed_letters.append(user_letter)
        if user_letter == 'exit':
            print(f'You lost, word to guess was: {word}, game round = {game_round}')
            draw(9)
            play_again()
            check = False
        elif user_letter == word:
            print(f'You win, You guess the word! It was {word}, game round = {game_round}')
            play_again()
            check = True

        else:
            for position, letter in enumerate(word):
                if user_letter == letter:
                    hidden_word[position] = letter
            if ''.join(hidden_word) == word:
                print('Word to guess: ', ' '.join(hidden_word))
                print(f'You won, the word to guess was: {word}, game round = {game_round}')
                play_again()
                check = True
        game_round += 1
    if game_round == 9:
        play_again()


hangman()
