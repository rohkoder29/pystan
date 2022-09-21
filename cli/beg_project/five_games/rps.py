from random import choice


def validate_choice(options) -> str:
    while 1:
        user_choice = input("Play [rock, paper or scissors]: ").lower()
        try:
            assert user_choice in options
        except AssertionError:
            print("Please choose a valid option.")
        else:
            return user_choice


def playing(turn: int, user_choice: str, cpu_choice: str):
    if cpu_choice == user_choice:
        print(f"CPU also chose {cpu_choice}")
        print("That's a tie.")
        return None
    if cpu_choice == "rock" and user_choice != "paper":
        print(f"You chose {user_choice} and CPU chose rock.")
        print("Rock breaks scissors.")
        print("You Lost.")
        return None
    if cpu_choice == "paper" and user_choice != "scissors":
        print(f"You chose {user_choice} and CPU chose paper.")
        print("Paper wraps rock.")
        print("You Lost.")
        return None
    if cpu_choice == "scissors" and user_choice != "rock":
        print(f"You chose {user_choice} and CPU chose scissors.")
        print("Scissors cut paper.")
        print("You Lost.")
        return None
    print(f"CPU chose {cpu_choice}")
    print(f"You won!! It took you {turn} round(s)!")
    return 1


def rock_paper_scissors(turn: int):
    options = ("rock", "paper", "scissors")
    while 1:
        user_choice = validate_choice(options)
        turn += 1
        cpu_choice = choice(options)
        if playing(turn, user_choice, cpu_choice):
            break
