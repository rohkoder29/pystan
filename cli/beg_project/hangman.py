"""
A SIMPLE IMPLEMENTATION OF THE FAMOUS HANGMAN GAME
"""

import json
from collections import Counter
from random import choice

with open("words.json", "r") as file:
    words = json.load(file)["data"]

secret_word = choice(words)

print("GUESS THE WORD TO WIN!")

for letter in secret_word:
    print("_", end=" ")
# print()

playing: bool = True
letter_guessed: list = []
chances: int = len(secret_word) + 2
correct: int = 0
complete: bool = False

while chances != 0 and not complete:
    print()
    chances -= 1

    # Validation of the guess
    try:
        guess = str(input("Enter a letter to guess: "))
        assert guess.isalpha() and len(guess) == 1
    except AssertionError:
        print("Please type in only one letter!")
        continue

    # If letter is guessed correctly
    if guess in secret_word:
        k = secret_word.count(guess)
        letter_guessed.extend(guess for _ in range(k))
    # Show the word
    for letter in secret_word:
        if letter in letter_guessed and Counter(letter_guessed) != Counter(
            secret_word
        ):
            print(letter, end=" ")
            correct += 1

    # If user has guessed all the letters
