from random import choice
from rich import print

file = "/path/to/five_games/wordle.txt"
with open(file, "r") as f:
    words = f.readlines()

class Wordle:
    def __init__(self) -> None:
        self.word = choice(words).rstrip("\r\n")
        self.num_guesses = 0
        self.dict_guesses = {
            0: [" "]*5,
            1: [" "]*5,
            2: [" "]*5,
            3: [" "]*5,
            4: [" "]*5
        }

    def draw_board(self):
        for guess in self.dict_guesses.values():
            print(" | ".join(guess))
            print(f"{' - ' * 6}")

    def get_user_input(self):
        try:
            user_guess = input("Enter a 5-letter English word: ").lower()
            assert len(user_guess) == 5
        except AssertionError:
            print("Invalid. Please enter a 5-letter English word: ")
        else:
            for idx, letter in enumerate(user_guess):
                if letter in self.word:
                    if letter == self.word[idx]:
                        letter = f"[green]{letter}[/]"    # green
                    else:
                        letter = f"[yellow]{letter}[/]"    # yellow
                self.dict_guesses[self.num_guesses][idx] = letter
            self.num_guesses += 1
            return user_guess

    def play(self):
        print(self.word)
        while 1:
            if not (user_guess := self.get_user_input()):
                continue
            self.draw_board()
            if self.num_guesses >= 5:
                print(f"You lost. Word was '{self.word}'.")
                break
            if user_guess == self.word:
                print(f"You won! Word is '{self.word}'.")
                break

# file = "/home/rohkuntu/Documents/year2022/python/cli/beg_project/five_games/wordle.txt"