import sqlite3


# CRUD: Create, Read, Update, Delete

# first we connect to database
# if doesn't exist, created
konekt = sqlite3.connect('customers.db')

# then we create a cursor
# we gonna call it 'kur'
kur = konekt.cursor()

# now it's time to create a table
# kur.execute("""CREATE TABLE customers (
# 		first_name TEXT,
# 		last_name TEXT,
# 		email TEXT,
# 		city TEXT)
# 	""")

# DATATYPE IN SQLite3
# NULL
# INTEGER
# REAL
# TEXT
# BLOB


### Inserting one record to the table
kur.execute(
    "INSERT INTO customers VALUES ('donsten','rohko',\
    'donsten_rohko@outlook.com','buenos aires')")


### Inserting many records to the table
# list_customers = [
# 				 	('amanda', 'wallace', 'amanda@wallace.com', 'sydney'),
# 				 	('john', 'goldberg', 'john@goldberg.com', 'new jersey'),
# 				 	('hazel', 'thornton', 'hazel@thornton.com', 'glasgow'),
# 				 	('serena', 'masterson', 'serena@masterson.com', 'bali')
# 				 ]
# kur.executemany("INSERT INTO customers VALUES (?,?,?,?)", list_customers)


## Query the database
# kur.execute("SELECT * FROM customers")
# kur.fetchone()
# kur.fetchmany(3)

## show all the data in the table
# customers = kur.fetchall()
# print(customers)

# print(kur.fetchone()) # grabs the first record encountered
# print(kur.fetchone()) # grabs the next one

# for customer in customers:
#     print(f"""First name: {customer[0]}\
# \nLast name: {customer[1]}\
# \nEmail address: {customer[2]}\
# \nCity : {customer[-1]}\
# \n--------------------------------------""")

# print('NAME', '\t\tCITY')
# print('-------', '\t---------')
# for customer in customers:
#     print(customer[0], customer[1] +'\t'+ customer[-1])


### primary key ID
# kur.execute("SELECT rowid, * FROM customers")
# customers = kur.fetchall()

# for customer in customers:
#     print(customer)


### WHERE clause
# kur.execute("SELECT * FROM customers WHERE city = 'sydney'")
# select all the data from table <customers> where last name ends with 'on'
# kur.execute("SELECT * FROM customers WHERE last_name LIKE '%on'")
# customers = kur.fetchall()

# for customer in customers:
#     print(customer)


### Update records
# consider using <rowid> for these operations
# kur.execute("""UPDATE customers SET first_name = 'dylan'
#             WHERE city = 'new jersey'
#         """)
# konekt.commit()

# kur.execute("""UPDATE customers SET email = 'dylan@goldberg.com'
#             WHERE email LIKE '%@goldberg.com'
#         """)
# konekt.commit()

# kur.execute("SELECT * FROM customers")
# customers = kur.fetchall()

# for customer in customers:
#     print(customer)


### Delete a record
# kur.execute("DELETE from customers WHERE rowid = 3")


### Order results by - ORDER BY
# order: ASCending or DESCending
# kur.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# kur.execute("SELECT rowid, * FROM customers ORDER BY last_name ASC")
# customers = kur.fetchall()

# for customer in customers:
#     print(customer)


### And / Or
# kur.execute("INSERT INTO customers VALUES ('amanda','darren','renanda@gmail.com','london')")
# konekt.commit()

# kur.execute("SELECT rowid, * FROM customers WHERE first_name = 'amanda' AND rowid = 6")
# kur.execute("SELECT rowid, * FROM customers WHERE city = 'london' OR city = 'glasgow'")

# customers = kur.fetchall()

# for customer in customers:
#     print(customer)


### Limiting results
# returns last two rows in descending order
# kur.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
# customers = kur.fetchall()

# for customer in customers:
#     print(customer)


### Drop a table
# kur.execute("DROP TABLE customers")
# konekt.commit()



###
# # commit our command
# konekt.commit()
# print('Command executed successfully...')

# # close our connection
# konekt.close()






# kur.execute("SELECT * FROM d_book")
# contacts = kur.fetchall()

# for contact in contacts:
#     print(contact[0], contact[1])


# COMMON ERRORS:

# Error
# DatabaseError
# DataError
# IntegrityError
# InternalError
# NotSupportedError
# OperationalError
# ProgrammingError
# InterfaceError
# Warning
