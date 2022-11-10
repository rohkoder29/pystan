import sqlite3 as lite


class Database:
    """ """
    def __init__(self, db_file='users.db', table_name='credentials') -> None:
        """ """
        ## enable connection to database
        self._conn = lite.connect(db_file)
        ## initialize the cursor
        self._curs = self._conn.cursor()
        ## create table table_name if not exists
        self._curs.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} \
                (application TEXT NOT NULL, \
                username TEXT NOT NULL, \
                password TEXT NOT NULL UNIQUE PRIMARY KEY, \
                salt TEXT NOT NULL)""")
        return None

    def add_credentials(self, app, username, password, salt) -> None:
        """ This method queries the database and add a record to it. """
        try:
            self._curs.execute(f"""INSERT INTO credentials VALUES \
                    (?, ?, ?, ?) """, (app, username, password, salt))
        except lite.IntegrityError:
            print("Record already exists in the table.")
        else:
            self._conn.commit()
        return None
    
    def show_entries(self) -> list:
        self._curs.execute("""SELECT * FROM credentials""")
        return self._curs.fetchall()

