import random
import re

def get_words():
    with open('lingowords.py', 'r') as f:
        content = f.read()
        words = re.findall(r'\b\w+\b', content)
        return words

def select_word():
    return random.choice(get_words())

def check_guess(word, guess, correct_letters):
    if len(guess) != len(word):
        print('Invalid guess length')
        return False
    if word.lower() == guess.lower():
        return True
    word = word.replace('Ĳ', 'Y')
    guess = guess.replace('Ĳ', 'Y')
    num_correct = 0
    hint = ''
    for i in range(len(word)):
        if i in correct_letters:
            hint += '\033[32m' + word[i] + '\033[0m'
            num_correct += 1
        elif word[i].lower() == guess[i].lower() or (word[i].isdigit() and guess[i].isdigit()):
            if i not in correct_letters:
                hint += '\033[32m' + word[i] + '\033[0m'
                correct_letters.add(i)
                num_correct += 1
            else:
                hint += '\033[33m' + guess[i] + '\033[0m'
        elif guess[i] in word:
            hint += '\033[33m' + guess[i] + '\033[0m'
        else:
            hint += '_'
    print('Hint:', hint)
    return False if num_correct != len(word) else True

def start_game():
    word = select_word()
    print(f'The word has {len(word)} letters')
    print(f'First letter: {word[0]}')
    correct_letters = set()
    for i in range(1, 6):
        guess = input(f'Guess {i}: ')
        if check_guess(word, guess, correct_letters):
            print('Congratulations, you guessed the word!')
            return
    print(f'Sorry, you ran out of guesses. The word was {word}')

start_game()