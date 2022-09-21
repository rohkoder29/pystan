# from time import sleep
# from random import randint

# p1 = 0
# p3 = 0
# while True:
#     p1 += randint(-1, 1)
#     p2 = randint(-10, 10)
#     # p3 = randint(p2, abs(p1 + p2))
#     p3 += 1
#     print("Random walk:", p1, " just random:", p2, " times", p3)
#     sleep(.25)

#############################

# import numpy as np
#
# # word = input('Input a word: ').upper()
# word = 'landon'.upper()
# size = len(word)
# print(word, size)
#
# diagram = np.empty([len(word), len(word)], dtype=np.str0)
# print(diagram)
#
# for i, j in enumerate(word):
#     diagram[[i], [0]] = j
#
# for i, j in enumerate(word):
#     diagram[[0], [i]] = j
#
# print(diagram)
#
# letters = list(word)
# size = len(letters)
# print(letters)
