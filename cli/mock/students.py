"""
A program that takes a 1,000 students and figure out cool stuff about them
"""

""" CSV """

# # from json import load

# # # read the json file
# # file_path = '/home/rohkuntu/Documents/year2022/py/cli/mock/students.json'
# # with open(file_path, 'r') as file:
# #   data = load(file)

# # count = 0
# # for i in range(len(data)):
# #   if int(data[i]['date_of_birth'][-4:]) > 1997:
# #     print(data[i]['first_name'])
# #     count += 1

# # print(count)

# ### with request

# # import urllib.request
# # from io import StringIO
# # from csv import reader
# # # from collections import Counter

# # url = "https://api.mockaroo.com/api/726c5e00?count=589&key=4a80d0c0"

# # try:
# #   with urllib.request.urlopen(url) as data:
# #     dhand = StringIO(data.read().decode('utf-8').strip())
# #     csvReader = reader(dhand)
# # except urllib.error.URLError as e:
# #   print(e.reason)

# # records = list(csvReader)
# # # print(records)

# # # # how many students
# # stud = len(records)

# # count = sum(i[6] == 'Architecture' for i in records)
# # print(f'{count} students ->  ~ {round((count/stud), 2)}%')

# ### with pandas

# # import pandas as pd

# # url = "https://api.mockaroo.com/api/726c5e00?count=1000&key=4a80d0c0"

# # df = pd.read_csv(url)

# # df.info()

# ### with numpy

# # import numpy as np

# # npdata = np.genfromtxt(
# #     'https://api.mockaroo.com/api/726c5e00?count=1000&key=4a80d0c0', dtype=np.str0, delimiter=',')

# # count = sum(1 for i in npdata if i[4] == 'Male' and i[-1])
# # print(count)

# #############################

import urllib.request
from io import StringIO
from csv import reader
import numpy as np
from collections import Counter

url = "https://api.mockaroo.com/api/726c5e00?count=100&key=4a80d0c0"

try:
    with urllib.request.urlopen(url) as data:
        dhand = StringIO(data.read().decode("utf-8").strip())
        csvReader = reader(dhand)
except urllib.error.URLError as e:
    print(e.reason)

records = list(csvReader)

stud = len(records)
nprecords = np.array(records, dtype=np.str0)

# sport and house affiliation
# count = 0
# elite = []
# for i in range(len(nprecords)):
#     if nprecords[i][-1] and nprecords[i][7]:
#         count += 1
#         elite.append(nprecords[i][7:])
# # print(f'{count} students on {stud} =>  ~ {round((count/stud)*100, 2)}%')
# print(elite[0], len(elite), type(elite))

# mock = []
# for item in elite:
#   mock.append(item)
# print(mock[0], len(mock), type(mock))

# elite == mock


# ''' JSON  '''
#
# import json
#
# with open('students.json', 'r') as file:
#   data = json.load(file)
#
# print(type(data), len(data))
# print(data[0])
#
# count = 0
# for row in data:
#   if row['sport'] == 'Football':
#     print(row['id'])
#     count += 1
# print(count)
