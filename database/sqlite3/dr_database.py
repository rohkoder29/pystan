import sqlite3

db = "/home/rohkoder29/Documents/year2022/python/database/sqlite3/d_book.db"

# query DB and return all the records
def show_all():
    """  docstring  """
    konekt = sqlite3.connect(db)
    kur = konekt.cursor()
    # query the DB
    kur.execute("SELECT rowid, * FROM d_book ORDER BY last_name")
    contacts = kur.fetchall()
    # print to screen
    for contact in contacts:
        print(contact)
    # commit our command
    konekt.commit()
    # close our connection
    konekt.close()


def add_record(first_name, last_name, tel_number, e_mail, rsdnc):
    """  docstring  """
    # enable connection to DB and create cursor
    konekt = sqlite3.connect(db)
    kur = konekt.cursor()
    # insert values to the table
    kur.execute(
        "INSERT INTO d_book VALUES (?,?,?,?,?)",
        (first_name, last_name, tel_number, e_mail, rsdnc),
    )
    # commit command and shut down connection
    konekt.commit()
    konekt.close()


def add_many():
    """  docstring  """
    # enable connection to DB and create cursor
    konekt = sqlite3.connect(db)
    kur = konekt.cursor()
    # insert values to the table
    kur.executemany("INSERT INTO d_book VALUES (?,?,?,?,?)", (list))
    # commit command and shut down connection
    konekt.commit()
    konekt.close()


def update_record(tel_number, first_name):
    """  docstring  """
    # enable connection to DB and create cursor
    konekt = sqlite3.connect(db)
    kur = konekt.cursor()
    # insert values to the table
    kur.execute(
        """UPDATE d_book SET tel_number = (?)
        WHERE first_name = (?)""",
        (tel_number, first_name),
    )
    # commit command and shut down connection
    konekt.commit()
    konekt.close()


def del_record(i_d):
    """  docstring  """
    konekt = sqlite3.connect(db)
    kur = konekt.cursor()
    kur.execute("DELETE from d_book WHERE rowid = (?)", i_d)
    konekt.commit()
    konekt.close()


def look_up(first_name):
    """  docstring  """
    konekt = sqlite3.connect(db)
    kur = konekt.cursor()
    # query the DB
    kur.execute("SELECT rowid, * FROM d_book WHERE first_name = (?)", (first_name,))
    contacts = kur.fetchall()
    # print to screen
    for contact in contacts:
        print(contact)
