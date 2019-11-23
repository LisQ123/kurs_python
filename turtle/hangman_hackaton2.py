import random


def word_choice():
    words = []
    with open('hasla.txt', 'r') as fopen:
        all_words = fopen.readlines()
        words.append(all_words)
        for i in words:
            chosen_word = random.choice(i)
    return chosen_word


def hangman():
    print('Welcome to hangman game')
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    print('Letters to use: ', alphabet)
    word = word_choice()
    len_word = []
    for letter in word:
        len_word.append('_')
    try_to_guess = False
    game_round = 1
    while not try_to_guess:
        print('Word to guess: ', ' '.join(len_word))
        user_letter = input('Give me a letter, to quit write - exit ')
        if user_letter == 'exit':
            print(f'You lost, word to guess was: {word}, game round = {game_round}')
            try_to_guess = True
        elif user_letter == word:
            print(f'You win, You guess the word! It was {word}, game round = {game_round}')
            try_to_guess = True

        else:
            for position, letter in enumerate(word):
                if user_letter == letter:
                    len_word[position] = letter
            if ''.join(len_word) == word:
                print('Word to guess: ', ' '.join(len_word))
                print(f'You won, the word to guess was: {word}, game round = {game_round}')
                try_to_guess = True
        game_round += 1
    play_again()


def play_again():
    question = input('Do you want to play again? yes/no ')
    if question.lower() == 'yes':
        hangman()
    else:
        exit()


hangman()
