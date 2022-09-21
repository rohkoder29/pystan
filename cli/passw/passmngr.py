import os
import sys
import csv
import secrets
import random
import string


print("\nWELCOME TO THE PASSWORD GENERATOR APP\n")
ALPHABET = list(string.ascii_letters)
NUMBERS = list(string.digits)
SYMBOLS = list("!@#~|$%&*?")

while 1:

    MENU = """\nChose an operation:
    1. Generate new password
    2. Show all passwords
    3. Modify a password
    4. Exit

    >>>>>> """

    option = input(MENU)

    match option:
        case '1':

            pass_use = input("Password usage: ")
            # catch and control password length recommendations due to rules

            while 1:
                PASS_LEN = int(
                    input("How long do you want your password to be \
                        (min 8, max 15 characters): "))
                if PASS_LEN not in range(8, 16):
                    print("Password length must be from 8 to 15 characters long.")
                    continue
                while 1:
                    PASS_CHARS = int(input("How many letters: "))
                    PASS_NUMS = int(input("How many numbers: "))
                    PASS_SYMS = int(input("How many symbols: "))

                    # check whether user respected configuration limits
                    if PASS_LEN != (PASS_CHARS + PASS_NUMS + PASS_SYMS):
                        print("Password has wrong config, letter + number +\
                            symbol must match password length.")
                        continue
                    break
                break

            # generating values

            CHARS_PASS = [secrets.choice(ALPHABET) for _ in range(PASS_CHARS)]
            NUMS_PASS = [secrets.choice(NUMBERS) for _ in range(PASS_NUMS)]
            SYMS_PASS = [secrets.choice(SYMBOLS) for _ in range(PASS_SYMS)]

            # concatenate values

            PASS_PHRASE = CHARS_PASS + NUMS_PASS + SYMS_PASS
            print(len(PASS_PHRASE))

            # randomize password

            random.shuffle(PASS_PHRASE)

            # transform list items into a string

            PASSWORD = "".join(PASS_PHRASE)
            print("Your generated password:", PASSWORD)

            # save password

            with open('passmngr.csv', 'a', newline='') as passmngr:
                pass_entry = csv.writer(passmngr)
                pass_entry.writerow(PASSWORD)

        case '2':
            print("show")
        case '3':
            print("edit")
        case '4':
            print("exit")
            sys.exit()
