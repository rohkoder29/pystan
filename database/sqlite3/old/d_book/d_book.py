# -*- coding: utf-8 -*-

"""
- VERSION WITH DATABASE (USING PYTHON BUILT-IN SQLITE3 MODULE)
- PROJECT AWAITS TO BE REVIEWED, REFACTORED AND VALIDED
- BUT UNTIL THEN, EVERYTHING WORKS CORRECTLY AS EXPECTED
    *** VERSION NOTES ***
    # TO BE ADDED:
    - PHONE NUMBER PATTERN VERIFICATION BY REGEX
    # TO BE REVIEWED (IN PRIORITY ORDER):
    - CONTACT DELETETION FUNCTION
    - CONTACT NAME PATTERN VERIFICATION BY REGEX
"""

import sqlite3
import sys
import re

# ^[A-Za-z][A-Za-z\'\-]+([\ A-Za-z][A-Za-z\'\-]+)*$

REGEX_NAME = r"^[A-Za-z][A-Za-z\'\-]+[\ A-Za-z][A-Za-z\'\-]*$"
REGEX_MAIL = r"(?i)^[a-z]+[-_$.a-z0-9]+@[a-z]*\.[a-z]{2,}$"
# REGEX_PHONE = r"""(\+91[\s-]\d{5}[\s-]\d{5})|(011[\s-]\d{8})|
# (\+91\d{2}[\s-]\d{8})|(^0\d{10})|(^[6-9]\d{9})|(91[\s-]\d{3,5}
# [\s-]\d{2,5}[\s-]\d{4})|(91[\s-]\d{5}[\s-]\d{5})|(91[\s-]\d{10})
# |(\d{4}[\s-]\d{4}[\s-]\d{3})"""
KEYS = ['first_name', 'last_name', 'tel_number', 'email', 'city']


def validate_option(option):
    """ docstring """
    while option not in str(list((range(1, 8))))[1:-1]:
        print('ERROR.\nPlease choose a valid option between 1 and 6.')
        option = input('>>>>>>> ')
    return int(option)


def first_input():
    """ docstring """
    first_name = input('First name: ')
    while first_name not in re.findall(REGEX_NAME, first_name):
    # while not first_name:
        print('ERROR.\nPlease input a correct first name.')
        first_name = input('First name: ')
    return first_name.lower()


def last_input():
    """ docstring """
    last_name = input('Last name: ')
    # while last_name not in re.findall(REGEX_NAME, last_name):
    while not last_name:
        print('ERROR.\nPlease input a correct last name.')
        last_name = input('Last name: ')
    return last_name.lower()


def tel_input():
    """ docstring """
    tel_number = input('Phone number (w/o spaces): ')
    while not isinstance(tel_number, (int, str)):
        print('ERROR.\nPlease input a correct phone number: ')
        tel_number = input()
    return tel_number


def email_input():
    """ docstring """
    email = input('Email address: ')
    while email not in re.findall(REGEX_MAIL, email):
        print('ERROR.\nPlease input a correct e-mail address: ')
        email = input()
    return email.lower()


def city_input():
    """ docstring """
    city = input('City: ')
    while not city:
        print('ERROR.\nPlease input a correct name: ')
        city = input()
    return city.lower()


def add_contact():
    """ Add a contact in the database. """
    # insert values to the table
    kur.execute("INSERT INTO d_book VALUES (?,?,?,?,?)",
        (first_input(),
         last_input(),
         tel_input(),
         email_input(),
         city_input()))
    # commit command
    konekt.commit()
    print('Operation OK!')


def edit_menu():
    """ Edit a contact details. """
    return """
EDIT MENU
1. First name
2. Last name
3. Phone number
4. Email address
5. City

[Enter 0 to cancel]

Select a number to update.
>>>>>>>>>  """


def validate_upd_option(edit):
    """ Valide option choice. """
    while edit not in str(list((range(1, 6))))[1:-1]:
        print('ERROR.\nPlease choose a valid option between 1 and 5.')
        edit = input('>>>>>>> ')
    return int(edit)


def update_contact():
    """ Update contact details. """
    c_f_query = (input('Contact first name: '))
    c_l_query = (input('Contact last name: '))
    kur.execute("SELECT rowid, * FROM d_book WHERE first_name = (?)\
        AND last_name = (?)", (c_f_query, c_l_query))
    if contacts := kur.fetchall():
        edit = input(edit_menu())
        if edit != '0':
            valid = validate_upd_option(edit)
            cols = ['first_name', 'last_name', 'tel_number', 'email', 'city']
            edit_op = [first_input, last_input, tel_input, email_input, city_input]
            update = edit_op[valid - 1]()
            kur.execute(f"""UPDATE d_book SET {cols[valid - 1]} = '{update}'\
                WHERE first_name = '{c_f_query}' AND last_name = '{c_l_query}'""")
            # commit command
            konekt.commit()
            print('Operation OK!')
        else:
            print('Operation canceled!')
    else:
        print('Contact not found.')


def show_all():
    """ Show all the contacts currently in the database. """
    # query the DB
    kur.execute("SELECT rowid, first_name, last_name FROM d_book ORDER BY last_name")
    contacts = kur.fetchall()
    # show
    print('   First Name\tLast Name')
    print('   ----------   ----------')
    for idx, contact in enumerate(contacts, start=1):
        print(f'{idx:>2}. {contact[1].title()}\t{contact[2].title()}')


def search_contact():
    """ Search a contact within the database. """
    # get query terms
    c_query = (input('Contact name: '))
    # query the DB
    kur.execute("SELECT rowid, * FROM d_book WHERE first_name LIKE '%'||?||'%'\
                OR last_name LIKE '%'||?||'%'", (c_query,c_query))
    if contacts := kur.fetchall():
        for contact in contacts:
            print('\n' + '* '*15)
            print(f"* {contact[2].title()}, {contact[1].title()}")
            print(f'* {contact[3]}')
            print(f'* {contact[4]}')
            print(f'* {contact[-1].title()}')
            print('* '*15)
    else:
        print('\nContact not found.')


def del_contact():
    """ Delete a contact from the database. """
    c_query = (input('Contact name: '))
    # query the DB
    kur.execute("SELECT rowid, * FROM d_book WHERE first_name LIKE '%'||?||'%'\
        OR last_name LIKE '%'||?||'%'", (c_query,c_query))
    if contacts := kur.fetchall():
        kur.execute("DELETE FROM d_book WHERE first_name LIKE '%'||?||'%' OR \
            last_name LIKE '%'||?||'%'", (c_query,c_query))
        konekt.commit()
        print('Operation OK!')
    else:
        print('\nContact not found.')


def clear_db():
    """ Clear the database. """
    kur.execute("DROP TABLE d_book")
    konekt.commit()


def quit_program():
    """ Quit the program. """
    print('Hasta luego, friend.')
    # mesure de précaution
    sys.exit()


BOOK_OP = [add_contact, update_contact, show_all, search_contact,
           del_contact, clear_db, quit_program]
DB_PATH = '/home/rohkuntu/Documents/year2022/python/sqlite3/d_book/db_book.db'

MENU = '''\nChoose an option:
1. Add New Contact
2. Update Contact Info
3. Show Contact List
4. Search Contact
5. Delete Contact
6. Clear Contact List
7. Quit

>>>>>>> '''
while OPTION := input(MENU):
    is_valid = validate_option(OPTION)
    print('-' * 20)
    konekt = sqlite3.connect(DB_PATH)
    kur = konekt.cursor()
    BOOK_OP[is_valid - 1]()
    konekt.close()
print('Process terminated with code : -1')
