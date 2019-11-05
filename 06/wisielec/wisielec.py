import random
# words = {'animals': ['owca', 'kon', 'wielblad', 'koza', 'krowa'],
        # 'foods': ['jablko', 'chleb', 'ciasto', 'maslo','gruszka', 'bulka', 'mango'],
        # 'jobs': ['aptekarz', 'prawnik', 'lekarz', 'listonosz']}
words = []

with open('hasla.txt') as fopen:
    all_words = fopen.readlines()
    words.append(all_words)
print(words)

def menu():
    print('Welcome to hangmann game')
    print()
    category_name = False
    while not category_name:
        category = input('Please choose one of avaliable category of words: alimals, foods, jobs. ')
        if category not in words.keys():
            print('Please write correct name of category')
        else:
            category_name = True
    print(category)
    return category


def word_choice(category):
    chosen_word = random.choice(words[category])
    return chosen_word


def hangman():
    # print('Category: ') jak tutaj wydrukowac kategorie?
    category_choice = menu()
    word = word_choice(category_choice)
    underscore_word = []
    for letter in word:
        underscore_word.append('_')
    try_to_guess = False
    game_round = 1
    while not try_to_guess:
        print('Word to gues: ', ' '.join(underscore_word))
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
                    underscore_word[position] = letter
            if ''.join(underscore_word) == word:
                print('Word to gues: ', ' '.join(underscore_word))
                print(f'You won, the word to guess was: {word}, game round = {game_round}')
                try_to_guess = True
        game_round += 1
    play_again()


def play_again():
    question = input('Do you want to play again? y/n ')
    if question.lower() == 'y':
        hangman()
    else:
        exit()

hangman()