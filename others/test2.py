# anagram detector program

# def is_anagram(string1: str, string2: str) -> bool:
#   if len(string1) != len(string2):
#     return False
#   return set(string1.lower()) == set(string2.lower())
# # # or just
# # def are_anagrams(s1, s2):
# #   return False if len(s1) != len(s2) else set(s1.lower()) == set(s2.lower())


# word1 = input('Enter first word: ')
# word2 = input('Enter second word: ')

# if is_anagram(string1=word1, string2=word2):
#   print(f'{word2} is an anagram of {word1}')
# else:
#   print(f'{word2} is not an anagram of {word1}')

############

# Currency conversion // conversor de monedas
# from forex_python.converter import CurrencyRates
#
#
# def validar_opcion(entrada):
#   while True:
#     try:
#       entrada
#       assert entrada.isdigit() and int(entrada) in [1, 2, 3, 4]
#     except AssertionError:
#       print('Por favor elija una opcion entre 1, 2, 3 o 4.')
#       entrada = input(MENU)
#     else:
#       return int(entrada)
#
#
# def conversor(monto, tasa, entrada, salida):
#   pass
#
#
#
#
#
#
# MENU = '''Hola, este es el conversor de monedas!\n
# Elija una de las siguientes opciones colocando el numero correspondiente:
# 1. A dolar
# 2. A euro
# 3. A libra
# 4. Salir
# >>> '''
#
# opcion = input(MENU)
# validar_opcion(entrada=opcion)

################################

# res = [(2006, 'SpongeBob SquarePants', 3),
#        (2006, 'Star Wars', 11),
#        (2006, 'Super Heroes', 8),
#        (2007, 'Harry Potter', 1),
#        (2007, 'SpongeBob SquarePants', 2),
#        (2007, 'Star Wars', 16),
#        (2007, 'Super Heroes', 2),
#        (2008, 'Indiana Jones', 12),
#        (2008, 'SpongeBob SquarePants', 3),
#        (2008, 'Star Wars', 23),
#        (2008, 'Super Heroes', 5)]
#
# # adict = {}
# # for x, y, z in res:
# #     if x in adict:
# #         adict[x].append((x, y, z))
# #     else:
# #         adict[x] = [(x, y, z)]
# # max_count = [max(adict[i]) for i in adict]
# # print(max_count)
#
#
# [max([g for g in mylist if g[0] == year ], key= lambda k: k[2]) for year in list(set([g[0] for g in mylist]))]

#######################

# a = [4, 7, 2, 0, 3, 8]
# n = len(a)
#
# for i in range(1, n):
#         value = a[i]
#         j = i
#         while j > 0 and a[j - 1] > value:
#             a[j] = a[j - 1]
#             j -= 1
#         a[j] = value
# print(a)

######################

# from itertools import groupby
# from operator import itemgetter
#
# l_tup = [(2006, 'SpongeBob SquarePants', 3), (2006, 'Star Wars', 11), (2006, 'Super Heroes', 8), (2007, 'Harry Potter', 1), (2007, 'SpongeBob SquarePants', 2), (2007, 'Star Wars', 16), (2007, 'Super Heroes', 2), (2008, 'Indiana Jones', 12), (2008, 'SpongeBob SquarePants', 3), (2008, 'Star Wars', 23), (2008, 'Super Heroes', 5)]
#
# assert [max(list(g), key=itemgetter(2)) for k, g in groupby(l_tup, itemgetter(0))] == [(2006, 'Star Wars', 11), (2007, 'Star Wars', 16), (2008, 'Star Wars', 23)]

######################

# def place_value(number):
# #     return ("{:,}".format(number))
#     return f"{number:,.2f}"
#
# print(place_value(1010))

#######################
