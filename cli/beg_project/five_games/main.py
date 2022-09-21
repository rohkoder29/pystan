from sys import exit
from gtn import guess_the_number
from rps import rock_paper_scissors
from wordle import Wordle


def main():
    while 1:
        print(f"""{"- " * 16}
        Mini Games!!!\n
        1. Guess The Number
        2. Rock Paper Scissors
        3. Wordle
        4. Connect Four
        5. Tic Tac Toe
        6. Quit
        """)
        try:
            game = input("Choose a game: ")
            assert game.isnumeric() and int(game) in range(1, 7)
        except AssertionError:
            print("Please choose a valid option.")
            continue
        else:
            game = int(game)

        match game:
            case 1:
                print("\n\tTHIS IS THE NUMBER GUESSER GAME\n")
                bound = int(input("Choose your upper bound: "))
                guess_the_number(10, bound)
            case 2:
                print("\n\tTHIS IS THE ROCK-PAPER-SCISSORS GAME\n")
                rock_paper_scissors(0)
            case 3:
                print("\n\tTHIS IS THE WORDLE GAME\n")
                Wordle().play()
            case 4:
                print("Coming soon...")
            case 5:
                print("Coming soon...")
            case 6:
                print("Program exiting...")
                exit()


if __name__ == "__main__":
    main()
