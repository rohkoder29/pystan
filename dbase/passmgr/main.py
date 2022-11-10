#############################################
# THIS IS MY NEW PASSWORD MANAGER IN PYTHON #
#############################################

"""
   * Description of the project can be found in the README.me file attached to it.
   * Licensing information can be found in the LICENSE file attached to it.
"""

# Modules
import sys
from getpass import getpass
from password import Password
from database import Database
from textwrap import shorten
from tabulate import tabulate


def main(option) -> None:
    """ The main application """
    data_file, main_table = "users.db", "credentials"
    db = Database(data_file, main_table)
    match option:
        case "1":
            while True:
                try:
                    app = input("Where the password is going to be used? ")
                    assert app.isprintable()
                    username = input(f"Input your username or email for {app}: ")
                except AssertionError:
                    print("Please verify the input website/app name.")
                    continue
                else:
                    newPass = Password()
                    password = newPass.validate_password_input()
                    salt = newPass.create_salt()
                    salted_password = salt + password.encode("UTF-8")
                    # hashed_password = newPass.hash_password(salted_password)
                    # currently skipping the hashing step
                    peppered_password = newPass.encrypt_password(salted_password)
                    db.add_credentials(app, username, peppered_password, salt)
                    print("Record successfully added!")
                    break
        case "2":
            users = db.show_entries()
            columns = ["App", "Username", "Password"]
            table = []
            for x in users:
                table.append([x[0], x[1], shorten(str(x[2]), width=20, placeholder="*****")])
            print(tabulate(table, headers=columns, tablefmt="fancy_grid", showindex="always"))
            
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Exiting...")
            sys.exit()


if __name__ == "__main__":
    print("* PASSWORD MANAGER *")
    MENU = """
    Choose an option: 
        1 - Create a new credential
        2 - View saved credentials
        3 - Edit a saved credential
        4 - Delete a saved credential
        5 - Exit
    >>> """
    while True:
        master = getpass("Input your master password to unlock the vault: ")
        if master != "master":
            print("INCORRECT PASSWORD")
            continue
        else:
            while True:
                try:
                    option = input(MENU)
                    assert option in ["1", "2", "3", "4", "5"]
                except AssertionError:
                    print("Please choose a valid option.")
                else: 
                    # call the main function
                    main(option)
