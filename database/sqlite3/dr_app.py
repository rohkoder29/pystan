import dr_database



# add one record to the table
#dr_database.add_record('tim', 'doherty', '5541210', 'tim@doherty.com', 'silicon valley')

# add many records to the table
# records = [
# 			('joshua', 'keller', '556787412', 'josh@keller.com', 'swansea'),
# 			('elodie', 'moulin', '0654214078', 'elodie@moulin.com', 'paris')
# 		  ]

# dr_database.add_many(records)

# delete a record from the table
# make sure you type in a string, not int
#dr_database.del_record('3')
# 77844571
# update one record
dr_database.update_record('0245784512', 'giorgio')

# call the <show_all> function from the <dr_database> file
dr_database.show_all()

# search for a record
# dr_database.look_up('elena')
