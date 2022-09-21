# from rich import print

# name, age, w = "Kondhor", 23, 50

# print(f"{name!s} {name!r}")
# print(f"{name:>10}")
# print(f"{name} is {age} years old.")
# print(f"{name:^{w}}")


# def my_loop(desde, hasta, callback):
#     if desde <= hasta:
#         callback(desde, hasta)
#         my_loop(desde + 1, hasta, callback)


# def callback(desde, hasta):
#     print(f"This loop goes from {desde} to {hasta}")


# if __name__ == "__main__":
#     my_loop(0, 10, callback)

# list comprehension with filter
# syntax => [func(elem) for elem in iterable if cond(elem)]
#

#

# def high(number):
#     """ Returns a number if it is greater or equals to 5. """
#     if number >= 5:
#         return number

# numbers = [1.62, 2.72, 3.14, 6.02, 9.81]

# high_numbers = [high(number) for number in numbers if number >= 5]
# print(high_numbers)


# filtered = filter(high, numbers)

# high_numbers = []
# for number in filtered:
#     high_numbers.append(number)
# print(high_numbers)     # [6.02, 9.81]


# high_numbers = [number for number in numbers if high(number)]
# print(high_numbers)     # [6.02, 9.81]

###

# def sqrt(number):
#     """ Take the square root of a number. """
#     return number**(0.5)

# numbers = [1.62, 2.72, 3.14, 6.02, 9.81]

# s_numbers = [sqrt(number) for number in numbers if number >= 4]
# print(s_numbers)    # [2.453568829277059, 3.132091952673165]

###

# product_prices = {
#     'bread': 0.2,
#     'chocolate': 1,
#     'book': 20,
#     'car': 20_000
# }
# expensive = []

# for product, price in product_prices.items():
#     if price > 100:
#         expensive.append(product)

# print(expensive)    # ['car']

# # with list comprehension
# expensive = [product
#              for product, price in product_prices.items()
#              if price > 100]
# print(expensive)    # ['car']

###

# # sourcery skip: for-append-to-extend
# cash_flows = [100, 200, -300, 400, 500, -600]

# inflows = []
# for cash in cash_flows:
#     if cash > 0:
#         inflows.append(cash)

# print(inflows)      # [100, 200, 400, 500]


# # with list comp
# inflows = [cash for cash in cash_flows if cash > 0]
# print(inflows)      # [100, 200, 400, 500]


###

# string = "The QUICK brown FOX jumps."
# upper = []
# for word in string.split():
#     if word == word.upper():
#         upper.append(word)

# print(upper)    # ['QUICK', 'FOX']

# # with list comprehension
# upper = [word
#          for word in string.split()
#          if word == word.upper()]

# print(upper)    # ['QUICK', 'FOX']

###

# numbers = [1, 0, 2, 0, 0, 1, 0, -1, -2, 0]

# nonzero = []
# for num in numbers:
#     if num:
#         nonzero.append(num)

# print(nonzero)      # [1, 2, 1, -1, -2]

# # with list comprehension
# nonzero = [num for num in numbers if num]
# print(nonzero)      # [1, 2, 1, -1, -2]

###

# is_healthy = {
#     "sleeping": True, "exercising": True,
#     "smoking": False, "relaxing": True,
#     "following @mathsppblog on Twitter": True
# }

# toodoo = []
# for activity, recommended in is_healthy.items():
#     if recommended:
#         toodoo.append(activity)

# print(toodoo)
# # ['sleeping', 'exercising', 'relaxing', 'following @mathsppblog on Twitter']


# # with list comprehension
# toodoo = [activity
#         for activity, recommended in is_healthy.items()
#         if recommended]
# print(toodoo)
# # ['sleeping', 'exercising', 'relaxing', 'following @mathsppblog on Twitter']

###

# print(map(str, [42, 73, 0, 16, 10]))
# print(list(map(str, [42, 73, 0, 16, 10])))
# print([str(num) for num in [42, 73, 0, 16, 10]])

# print("Python" "is"    "amazing")

###

# letters = []

# for i in range(65, 91):
#     letters.append(chr(i).lower())

# print(letters)

# # 65-91 are upper case [A-Z] ASCII
# letters = [chr(i).lower() for i in range(65, 91)]
# print(letters)

# # 97-123 are lower case [a-z] ASCII
# letters = [chr(i) for i in range(97, 123)]
# print(letters)

# #
# import string

# letters = list(string.ascii_lowercase)
# print(list(letters))

###

# lowers = filter(lambda word: word == word.lower(),
#                   "the QUICK brown FOX jumps".split())
# print(list(lowers))

# #

# lowers = [word 
#           for word in "the QUICK brown FOX jumps".split() 
#           if word == word.lower()]
# print(lowers)

###

# from pathlib import Path

# file_paths = [
#     Path("folder/myfile.txt"), 
#     Path("folder/otherfile.txt"), 
#     Path("folder/data.csv")]

# txt_names = []

# for path in file_paths:
#     if path.suffix == ".txt":
#         txt_names.append(path.name)

# print(txt_names)    # ['myfile.txt', 'otherfile.txt']

# # list comprehension
# txt_names = [path.name 
#              for path in file_paths 
#              if path.suffix == ".txt"]
# print(txt_names)    # ['myfile.txt', 'otherfile.txt']

###

# def c_print(*args, **kwargs):
#     kwargs.setdefault("sep", "\n")
#     print(*args, **kwargs)

# print("This", "will", "be", "printed", "normally.")
# # This will be printed normally.

# c_print("This", "will", "be", "printed", "over", "new", "lines.")
# # [guess the output]

###

# names = ["john", "ana", "andrew", "albert", "mary"]

# capitalized = []

# for name in names:
#     if name[0] == "a":
#         capitalized.append(name.capitalize())

# print(capitalized) # ['Ana', 'Andrew', 'Albert']

# # same thing using list comprehension
# capitalized = [name.capitalize() 
#                for name in names 
#                if name[0] == "a"]
# print(capitalized) # ['Ana', 'Andrew', 'Albert']

# # [ALT] using `startswith` function
# # instead of slicing
# capitalized = [name.capitalize() 
#                for name in names 
#                if name.startswith("a")]
# print(capitalized) # ['Ana', 'Andrew', 'Albert']

###

# numbers = [42, 73, 0, 16, 10]

# where_even = []
# for idx, num in enumerate(numbers):
#     if num % 2 == 0:
#         where_even.append(idx)

# print(where_even)   # [0, 2, 3, 4]

# # with list comprehension
# where_even = [idx
#               for idx, num in enumerate(numbers)
#               if num % 2 == 0]
# print(where_even)   # [0, 2, 3, 4]

###

# numbers = [42, 73, 0, 16, 10]

# odd_squares = []

# for num in numbers:
#     if num % 2:
#         odd_squares.append(num ** 2)

# print(odd_squares)      # [5329]

# # with list comprehension
# odd_squares = [num ** 2
#                for num in numbers
#                if num % 2]

# print(odd_squares)      # [5329]

###

# firsts = ["Harry", "Ron", "Hermione"]
# lasts = ["Potter", "Weasley", "Granger"]

# names = []
# for first, last in zip(firsts, lasts):
#     if len(first) >= len(last):
#         names.append(first + " " + last)

# print(names)    # ['Hermione Granger']

# # with list comprehension
# # and using f-string instead of
# # string concatenation
# names = [f"{first} {last}"
#          for first, last
#          in zip(firsts, lasts)
#          if len(first) >= len(last)]

# print(names)    # ['Hermione Granger']

###

# colours = ("red", "green", "red", "yellow",
#            "purple", "green")
# rgb = ("red", "green", "blue")

# primary = []
# for colour in colours:
#     if colour in rgb:
#         primary.append(colour[0])

# print(primary)  # ['r', 'g', 'r', 'g']

# # with list comprehension
# primary = [colour[0].upper()
#            for colour in colours
#            if colour in rgb]

# print(primary)  # ['R', 'G', 'R', 'G']

##

# from pathlib import Path

# paths = [
#     Path("folder/myfile.txt"),
#     Path("folder"),
#     Path("other_folder/data.csv"),
#     Path("other_folder")
# ]

# filenames = [path.name 
#              for path in paths 
#              if path.suffix]

# print(filenames)    # ['myfile.txt', 'data.csv']

# # using greedy raw for-loop
# filenames = []
# for path in paths:
#     if path.suffix:
#         filenames.append(path.name)

# print(filenames)    # ['myfile.txt', 'data.csv']

###

# # list comps
# doubled_idx = [2 * idx 
#     for idx, num in enumerate(range(10, 100, 13)) 
#     if num % 2 == 0]

# print(doubled_idx)     # [0, 4, 8, 12]

# # standard for-loop
# doubled_idx = []
# for idx, num in enumerate(range(10, 100, 13)):
#     if not num % 2:
#         doubled_idx.append(idx * 2)

# print(doubled_idx)     # [0, 4, 8, 12]

###

# numbers = [42, 73, 0, 16, 10]

# square_roots = [num ** 0.5
#                 for num in numbers
#                 if num > 15]
# print(square_roots)
# # [6.48074069840786, 8.54400374531753, 4.0]

# # standard for-loop
# square_roots = []
# for num in numbers:
#     if num > 15:
#         square_roots.append(pow(num, 0.5))

# print(square_roots)
# # [6.48074069840786, 8.54400374531753, 4.0]

###

# firsts = ["Marie", "Albert", "Charles"]
# lasts = ["Curie", "Einstein", "Darwin"]

# names = [f + " " + l
#          for f, l in zip(firsts, lasts)
#          if len(f) <= len(l)]

# print(names)
# # ['Marie Curie', 'Albert Einstein']

# names = []

# for f, l in zip(firsts, lasts):
#     if len(f) <= len(l):
#         names.append(f"{f} {l}")

# print(names)
# # ['Marie Curie', 'Albert Einstein']

### nope

# def isprime(n): 
#    return False if n<=1 else all(n % i != 0 for i in range(2, n))


# primes = [i for i in range(2, 312) if isprime(i)]

# print(primes, len(primes))

###

# colour_map = {
#     "r": "red",
#     "g": "green",
#     "b": "blue"
# }
# colours = "rgbbwaglr"

# # list comps
# colour_names = [colour_map[c]
#                 for c in colours
#                 if c in colour_map]
# print(colour_names)
# # ['red', 'green', 'blue', 'blue', 'green', 'red']

# # for-loop
# colour_names = []

# for c in colours:
#     if c in colour_map:
#         colour_names.append(colour_map[c])

# print(colour_names)
# # ['red', 'green', 'blue', 'blue', 'green', 'red']

###

# constants = [("e", 2.72), ("pi", 3.14), ("g", 9.81)]
# names = []

# for item in constants:
#     for elem in item:
#         if isinstance(elem, str):
#             names.append(elem)

# print(names)    # ['e', 'pi', 'g']

# # list comps
# names = [elem 
#          for item in constants 
#          for elem in item 
#          if isinstance(elem, str)]
# print(names)    # ['e', 'pi', 'g']

###

# count = []

# for i in range(1, 3, 2):
#     for j in range(-3, 2):
#         count.append(i + j)

# print(count)  # [-2, -1, 0, 1, 2]

# # list comps
# count = [i + j 
#            for i in range(1, 3, 2) 
#            for j in range(-3, 2)]
# print(count)  # [-2, -1, 0, 1, 2]

###

quotes = [
    {"Jack Twist": "I wish I knew how to quit you."},
    {"Darth Vader": "No, I'm your father."},
    {"The Terminator": "Hasta la vista, baby!"}]


authors = []

for quote in quotes:
    for author in quote.keys():
        for initial in author.split():
            authors.append(initial[0].upper())

print(authors)
