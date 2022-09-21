from random import randint

def guess_the_number(attempts: int, m_max: int):
    print("\nOkay, shall we begin!\n")
    m_min = 0
    magic_number = randint(0, m_max)
    print(magic_number)
    while 1:
        if attempts > 0:
            print(f"{attempts} attempts left")
            try:
                user_number = int(input(f"Choose a number between {m_min}-{m_max}: "))
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
                    print("Number is greater. Keep guessing.")
                else:
                    print("\tYay! You got it right.")
                    print(f"\tIt took you {abs(10 - attempts)} attempts.")
                    break
        else:
            print("\tNo more attempts left. You lost.")
            break
