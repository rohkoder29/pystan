# A CLI-based rock-paper-scissors game.
# You play until you win.
# It will not be considered a turn if the user inputs something
# that's not in the available options, like "Spock".


from random import choice

def validate_choice() -> str | None:
    """ This function ensures the user has chosen either rock, paper or scissors.
    It takes no arguments and returns the user's choice.
    Raises an error if user inputs any value other than those mentioned above. """
    while 1:
        user_choice = input("Play [rock, paper or scissors]: ").lower()
        try:
            assert user_choice in options
        except AssertionError:
            print("Please choose a valid option.")
        else:
            return user_choice


def playing(turn: int, user_choice: str, cpu_choice: str) -> (int | None):
    """ Play Rock-Paper-Scissors game against the computer.\n
    Args:
    \t:param turn: int, the turn being played
    \t:param user_choice: str, the option chosen by the user
    \t:param cpu_choice: str, the option chosen by the computer\n
    Return:
    \t:return: int | None, if user wins returns 1, else returns None
    """
    if cpu_choice == user_choice:
        # print(f"CPU chose {cpu_choice}")
        print("That's a tie.")
        return None
    elif cpu_choice == "rock" and user_choice != "paper":
        # print(f"You chose {user_choice} and CPU chose rock.")
        print("Rock breaks scissors.")
        print("You Lost.")
        return None
    elif cpu_choice == "paper" and user_choice != "scissors":
        # print(f"You chose {user_choice} and CPU chose paper.")
        print("Paper wraps rock.")
        print("You Lost.")
        return None
    elif cpu_choice == "scissors" and user_choice != "rock":
        # print(f"You chose {user_choice} and CPU chose scissors.")
        print("Scissors cut paper.")
        print("You Lost.")
        return None
    # print(f"CPU chose {cpu_choice}")
    print(f"You won afer {turn} round(s)!")
    return 1


def main(turn: int) -> None:
    """ Entry point of the program.\n
    Args:
    \t:param turn: int, the turn being played"""
    while 1:
        user_choice = validate_choice()
        turn += 1
        cpu_choice = choice(options)
        if playing(turn, user_choice, cpu_choice):
            break


if __name__ == "__main__":
    print("\n\tWELCOME TO THE ROCK PAPER SCISSORS GAME\n")
    options = ["rock", "paper", "scissors"]
    RPS = 0     # RPS => Rock | Paper | Scissors
    main(RPS)
