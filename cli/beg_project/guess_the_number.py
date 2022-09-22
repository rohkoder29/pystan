#!/usr/bin/env python3
"""
  A nice CLI-based game to guess a randomly generated number between 0 and 100 (including both endpoints).
  You have 10 attempts to guess that number. Guess it before then like a Boss or lose like a perky little b!tch.
  version 1.2

  TODO: (version 1.3) number of attempts to be the result of the implementation of the Binary Search algorithm
"""


from random import randint


def play(attempts: int) -> None:
    """ Play the famous game. """
    m_min = 0
    m_max = 100
    while True:
        if attempts > 0:
            print(f"{attempts} attempts left")
            try:
                user_number = int(input(f"Please choose a number between {m_min}-{m_max}: "))
            except ValueError:
                print("Error. Please input an integer.")
            else:
                if user_number > 100 or user_number < 0:
                    continue
                attempts -= 1
                if magic_number < user_number:
                    if user_number < m_max:
                        m_max = user_number
                    print("Number is less. Keep guessing.")
                elif magic_number > user_number:
                    if user_number > m_min:
                        m_min = user_number
                    print("Number is greater. keep guessing.")
                else:
                    print("\tYay! You got it right.")
                    print(f"\tIt took you {abs(10 - attempts)} attempts.")
                    break
        else:
            print("\tNo more attempts left. You lost.")
            break


if __name__ == '__main__':
    print("\n\tWELCOME TO THE NUMBER GUESSER GAME\n")
    print("\nOkay let's get started, shall we?\n")
    ATTEMPTS = 10
    magic_number = randint(0, 100)
    play(ATTEMPTS)
