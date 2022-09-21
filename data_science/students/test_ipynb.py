# import pandas as pd
# from random import choice
#
# df1 = pd.read_csv('stud5k.csv')
# df2 = pd.read_csv('2stud5k.csv')
#
# frames = [df2, df1]
# df = pd.concat(frames, ignore_index=True, verify_integrity=True)
#
# indexes = df.id.to_list()
# dups = df.id.duplicated().to_list()
#
# def create_non_dup_id():
#     for a in range(len(dups)):
#         new_idx = f'{choice(range(111, 120))}-0{choice(range(1, 10))}-{choice(range(1000, 10000))}'
#         for i in indexes:
#             if i in dups:
#                 i = new_idx
#                 continue
#
# create_non_dup_id()

#########################

# from itertools import groupby
# from operator import itemgetter

# listed = [(1999, 'Star Wars', 13), (2000, "Disney's Mickey Mouse", 5), (2000, 'Star Wars', 26), (2001, 'Harry Potter', 11), (2001, 'Star Wars', 14), (2002, 'Harry Potter', 19), (2002, 'Star Wars', 28), (2002, 'Super Heroes', 3), (2003, 'Harry Potter', 3), (2003, 'Star Wars', 32), (2003, 'Super Heroes', 5), (2004, 'Harry Potter', 14), (2004, 'Star Wars', 20), (2004, 'Super Heroes', 6), (2005, "Disney's Mickey Mouse", 1), (2005, 'Harry Potter', 5), (2005, 'Star Wars', 28), (2005, 'Super Heroes', 1), (2006, 'Avatar', 2), (2006, 'SpongeBob SquarePants', 3), (2006, 'Star Wars', 11), (2006, 'Super Heroes', 8), (2007, 'Harry Potter', 1), (2007, 'SpongeBob SquarePants', 2), (2007, 'Star Wars', 16), (2007, 'Super Heroes', 2), (2008, 'Indiana Jones', 12), (2008, 'SpongeBob SquarePants', 3), (2008, 'Star Wars', 23), (2008, 'Super Heroes', 5), (2009, 'Indiana Jones', 7), (2009, 'SpongeBob SquarePants', 2), (2009, 'Star Wars', 39), (2010, 'Ben 10', 6), (2010, 'Harry Potter', 6), (2010, 'Prince of Persia', 6), (2010, 'Star Wars', 30), (2010, 'Toy Story', 15), (2011, 'Cars', 18), (2011, 'Harry Potter', 8), (2011, 'Pirates of the Caribbean', 16), (2011, 'SpongeBob SquarePants', 2), (2011, 'Star Wars', 32), (2011, 'Super Heroes', 5), (2012, 'Cars', 9), (2012, 'Minecraft', 1), (2012, 'SpongeBob SquarePants', 2), (2012, 'Star Wars', 43), (2012, 'Super Heroes', 32), (2012, 'Teenage Mutant Ninja Turtles', 2), (2012, 'The Hobbit and Lord of the Rings', 20), (2013, 'Minecraft', 2), (2013, 'Star Wars', 35), (2013, 'Super Heroes', 19), (2013, 'Teenage Mutant Ninja Turtles', 9), (2013, 'The Hobbit and Lord of the Rings', 13), (2013, 'The Lone Ranger', 8), (2014, 'Disney Princess', 8), (2014, 'Minecraft', 7), (2014, 'Star Wars', 45), (2014, 'Super Heroes', 23), (2014, 'Teenage Mutant Ninja Turtles', 10), (2014, 'The Hobbit and Lord of the Rings', 6), (2015, 'Disney Princess', 4), (2015, 'Jurassic World', 7), (2015, 'Minecraft', 4), (2015, 'Scooby-Doo', 5), (2015, 'Star Wars', 58), (2015, 'Super Heroes', 28), (2015, 'The Hobbit and Lord of the Rings', 1), (2016, 'Angry Birds', 6), (2016, 'Disney', 1), (2016, 'Disney Princess', 11), (2016, 'Ghostbusters', 1), (2016, 'Minecraft', 7), (2016, 'Scooby-Doo', 1), (2016, 'Star Wars', 61), (2016, 'Super Heroes', 33), (2017, 'Disney Princess', 6), (2017, 'Minecraft', 9), (2017, 'Pirates of the Caribbean', 1), (2017, 'Star Wars', 55), (2017, 'Super Heroes', 72)]
#
# res = []
# for _, group in groupby(listed, itemgetter(0)):
#     res.append(max(group, key=itemgetter(2)))
# print(res)

##########################

# elements = [(2006, 'SpongeBob SquarePants', 3), (2006, 'Star Wars', 11), (2006, 'Super Heroes', 8), (2007, 'Harry Potter', 1), (2007, 'SpongeBob SquarePants', 2), (2007, 'Star Wars', 16), (2007, 'Super Heroes', 2), (2008, 'Indiana Jones', 12), (2008, 'SpongeBob SquarePants', 3), (2008, 'Star Wars', 23), (2008, 'Super Heroes', 5)]
#
# n_elements = {}
# for element in elements:
#     cle = element[0]
#     if cle not in n_elements:
#         n_elements[cle] = []
#     n_elements[cle].append(element)
# resultat = [max(v, key=lambda x: x[2]) for v in n_elements.values()]
# print(resultat)

############################

# import pandas as pd
# from random import randint
#
# df = pd.read_csv('students10k.csv', index_col=False)
#
# dups_ids = df.loc[df.ID.duplicated()]['ID'].to_list()
# def change_dupd_ids(id):
#     if id in dups_ids:
#         id = f'{randint(111, 119)}-0{randint(1, 9)}-{randint(1000, 9999)}'
#         return id
#
# print(len(dups_ids))
#
# df.ID = df.ID.apply(lambda x: change_dupd_ids(x))
#
# print(len(dups_ids))

##########################

# from uuid import uuid4
#
# students = 10
# ids = set()
# while len(ids) < students:
#     ids.add(str(uuid4())[:8])
# print(ids)

##########################
# import pandas as pd
# import gender_guesser.detector as gender
# from random import choice
#
# df = pd.read_csv('students10k.csv', index_col=False)
# mf_df = df.loc[df.Gender.isin(['Male', 'Female'])]
# d = gender.Detector()
#
# def genderize(name):
#     gender = d.get_gender(name).title()
#     if gender not in ['Male', 'Female']:
#         return choice(['Non-binary', 'Agender', 'Polygender', 'Bigender', 'Genderqueer', 'Genderfluid'])
#     return gender
#
# mf_df['First Name'].apply(lambda x: genderize(x))

##########################
