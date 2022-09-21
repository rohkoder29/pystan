# import numpy as np
# import sys
# import timeit
# from rich import print
# import re
# import random

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# tinytuple = (123, 'techbeamers')
# print(3//5)

# msg = 'hi'
# fill = 's'
# align = '<'
# width = 10
# print(f'{msg:{fill}{align}{width}}')

# fdict = {'sum': lambda x, y: x + y,
#          'subtract': lambda x, y: x - y}
# print(fdict['sum'](1, 2))
# print(fdict['subtract'](2, 1))
# print(fdict['sum'](1, 5) + fdict['subtract'](2, -3))

# print('\N{chicken}')


# def main():
#   while True:
#     dice_in = input('Enter the dice (q to quit): ')
#     if dice_in.lower() == 'q':
#       break
#     low = eval(re.sub(r'd\d+', '*1', dice_in).lstrip('*'))
#     high = eval(dice_in.replace('d', '*').lstrip('*'))
#     dice_out = random.randint(low, high)
#     print(f'[{dice_in}] -> {dice_out}')


# if __name__ == '__main__':
#   main()

# nplist = np.arange(1, 10)
# # print(f'{nplist} -> {sys.getsizeof(nplist)} bytes')
# #
# stdlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(f'{stdlist} -> {sys.getsizeof(stdlist)} bytes')

# nplist2 = np.arange(1, 10).reshape(3, 3)
# # print(f'{nplist2} -> {sys.getsizeof(nplist)} bytes')
# #
# stdlist2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print(f'{stdlist2} -> {sys.getsizeof(stdlist)} bytes')

# print(f'{timeit.timeit(stmt="[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]", number=1000000)*1000} ms')
# print(
#     f'{timeit.timeit(stmt="[[1, 2, 3], [4, 5, 6], [7, 8, 9]]", number=1000000)*1000} ms')

# myset = set([1,2,3])
# print(myset)


# my_set = {"apple", "banana", "cherry"}
# for i in my_set:
#     print(i)


# from timeit import default_timer as timer
# my_list = [str(i) for i in range(5)] * 1000000

# start = timer()
# a = "".join(my_list)
# end = timer()
# print(f"concatenate string with join(): {(end - start)*1000} ms")

# from collections import Counter

# elem = [random.randint(-100, 100) for _ in range(50)]
# # print(elem)
# random.shuffle(elem)
# # print(elem)

# counter = Counter(elem)

# print(counter, len(counter))
# # print(counter.most_common(3))
# # print(sorted(counter), len(sorted(counter)))  #uniq element
# # print(sorted(counter.elements()))
# print(sum(counter.values()))  #total of all counts
# print(counter[0])             #total of counts '0'
# del counter[0]                #remove all '10'

# mele = 'the quick brown fox jumps over the lazy dog'

# counter.update(mele)          #add an other counter to an existing one
# # print(counter, len(counter))
# counter.clear()               #well it does what it says
# print(counter, len(counter))

# A, B = [7, 13], [10, 8]
# prod = [(x, y) for x in A for y in B]
# print(prod)

# from itertools import groupby

# persons = [{'name': 'Tim', 'age': 28}, {'name': 'Dan', 'age': 25},
#            {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

# for key, group in groupby(persons, key=lambda x: x['age']):
#     print(key, list(group))

# def is_greater(x, y):
#     assert (x > y), 'x should be greater than y'
#     print(f'Yessir {x} > {y}')
#
# is_greater(6, 5)

# try:
#     a = 5 // 2
#     b = a + '2'
# except ZeroDivisionError as e:
#     print(f'Well, you can\'t do {e} my friend...')
# except TypeError as e:
#     print(f'Ouuuh {e}')
# else:
#     print(a, b)
#     print('We good.')
# finally:
#     print('ciao')
#     sys.exit()

# class ValueTooHighError(Exception):
#     pass
#
# def test_value(x):
#     if x > 10:
#         raise ValueTooHighError('Sorry, value is too high.')
#
# try:
#     test_value(11)
#     print('Yessir!')
# except ValueTooHighError as err:
#     print(err)

# import json
#
# with open('sample.json', 'r') as file:
#   person = json.load(file)
#   print(person)
#
# perSON = json.dumps(person, indent=4)
#
# with open('python.json', 'w')as f:
#   json.dump(perSON, f, indent=4)
#
# print(perSON)

# print(bool(bool((lambda a, b: a * b)(4, 5)) - bool(True)))

# for item in zip(range(1, 4), ['Python', 'JavaScript', 'Kotlin']):
#   print(item)

# languages = ['Python', 'JavaScript', 'Kotlin']
#
# for item in zip(range(1, len(languages) + 1), languages):
#   print(item)
#
# # print all items which contain an 'o'
# for i, item in enumerate(languages, start=1):
#   if 'o' in item:
#     print(f'({i}, \'{item}\')')

# langdict = dict(zip(range(len(languages)), languages))
# print(langdict)
# print(langdict.keys())

# languages = ['Python', 'JavaScript', 'Kotlin', 'C#', 'Rust', 'Go', 'PHP']
# rand = []
# for i in range(random.randint(3, 7)):
#   if random.randint(i, i+1) % 2 == 0:
#     rand.append(languages[i])
#   elif languages[-i] not in rand:
#     rand.append(languages[-i])
#
# print(f'Best programming languages {rand}')
# # randict = dict(zip(range(1, len(rand) + 1), rand))
# # print(randict)

# languages = ['Python', 'JavaScript', 'Kotlin', 'C#', 'Rust', 'C++', 'PHP']
# try:
#   random.shuffle(languages)
#   langdict = dict(zip(range(1, len(languages) + 1), languages, strict=True))
#   for item in zip(range(1, 4), langdict.values()):
#     print(item)
# except ValueError:
#   print('Error. Not allowed to zip iterables of different size.')

# numbers = range(3)
# output = {*numbers}
# print(output)

# keys = ['network', 'name', 'handle']
# values = ['twitter', 'rohkoder', 'ddg.com']
# d = {}
# for key, d[key] in zip(keys, values):
#     pass
# print(d)
# # or
# d = dict(zip(keys, values, strict=True))
# for key, value in enumerate(d):
#     print(value, d[value])
# # print(d)

# from tqdm import tqdm

# for _ in tqdm(range(1000000), desc='one million numbers', ascii=True):
#   pass


###

# # Iterative Binary Search Function method Python Implementation
# # It returns index of n in given list1 if present,
# # else returns -1
# def binary_search(list1, n):
#   low = 0
#   high = len(list1) - 1
#   mid = 0

#   while low <= high:
#     # for get integer result
#     mid = (high + low) // 2
#     # Check if n is present at mid
#     if list1[mid] < n:
#       low = mid + 1
#     # If n is greater, compare to the right of mid
#     elif list1[mid] > n:
#       high = mid - 1
#     # If n is smaller, compared to the left of mid
#     else:
#       return mid
#       # element was not present in the list, return -1
#   return -1


# # Initial list1
# list1 = [12, 24, 32, 39, 45, 50, 54]
# n = 45

# # Function call
# result = binary_search(list1, n)

# if result != -1:
#   print("Element is present at index", str(result))
# else:
#   print("Element is not present in list1")


# dataset = [random.randint(-4200, 4200) for _ in range(3650)]
# dataset.sort()
# print(dataset)


# # # #

# seq = [1, 3, 7, 1, 3, 8, 2, 4, 3, 5]
#
# for val in seq:
#   if val % 2 == 0:
#     print(f'Here: {val}')
#     break
# else:
#   print('Not here.')

# # #

# insert a number to a list without modifying the order
# from the python `bisect` module
# def insort_right(a, x, lo=0, hi=None):
#     """Insert item x in list a, and keep it sorted assuming a is sorted.
#     If x is already in a, insert it to the right of the rightmost x.
#     Optional args lo (default 0) and hi (default len(a)) bound the
#     slice of a to be searched.
#     """

#     if lo < 0:
#         raise ValueError('lo must be non-negative')
#     if hi is None:
#         hi = len(a)
#     while lo < hi:
#         mid = (lo+hi)//2
#         if x < a[mid]:
#             hi = mid
#         else:
#             lo = mid+1
#     a.insert(lo, x)

####

# import json
# from collections import Counter

# # we will count how many characters that is in the file
# # for a specific set of valid words

# # open the json file in read mode
# with open('/home/rohkuntu/Documents/year2022/py/cli/beg_project/words.json', 'r', newline='') as file:
#   words: list = json.load(file)['data']

# # show total words in the file
# print(len(words))

# # create a counter
# c = Counter(words)
# chars = 0
# removed = 0

# # loop upon the
# for i in c:
#   # consider words that contain only alpha characters
#   if ' ' not in i and '-' not in i:
#     # print(i)
#     # create a counter for the actual word
#     d = Counter(i)
#     # increment with the number of character of each word
#     chars += sum(d.values())
#   else:
#     words.remove(i)
#     removed += 1

# # show total characters in the file for considered words
# print(chars)
# # show total non considered words
# print(removed)
# # show total considered words
# print(len(words))

###
