import random
import string

amount = 3
vowels = 'eyuioa'
consonants = 'qwrtpsdfghjklzxcvbnm'
any_letter = string.ascii_lowercase
letters = []
total_output_num = 10

def get_letter(letter):
    if letter == 'v':
        return random.choice(vowels)
    if letter == 'c':
        return random.choice(consonants)
    if letter == 'a':
        return random.choice(any_letter)

def get_mode():
    for i in range(amount):
        letter = input("Please, enter 'v', 'c' or 'a' to choose what letters will newly generated word consist of))")
        letters.append(letter)

def start_generator():
    get_mode()
    for k in range(total_output_num):
        res = list(map(get_letter, letters))
        print("".join(res))


start_generator()
