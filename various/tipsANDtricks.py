# sourcery skip: collection-into-set, for-index-replacement,
# identity-comprehension, merge-comparisons, min-max-identity,
# remove-unused-enumerate, simplify-generator, use-join
import sys


# 1) Iterate with enumerate instead or range(len(x))

data = [1, 2, -4, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0
print(data)
#
data = [1, 2, -4, -3]
for idx, _ in enumerate(data):
    if data[idx] < 0:
        data[idx] = 0
print(data)

# 2) Use list comprehension instead of raw for loops

square = []
for i in range(10):
    square.append(i * i)
print(square)
#
square = [i * i for i in range(10)]
print(square)
#
print([i * i for i in range(10)])

# 3) Sort complex iterables with sorted()

digit = [3, 5, 1, 6, 9]
sorted_digit = sorted(digit)
print(sorted_digit)
#
digit = [3, 5, 1, 6, 9]
sorted_digit = sorted(digit, reverse=True)
print(sorted_digit)
#
print(sorted([3, 5, 1, 6, 9]))
##
people = [
    {"name": "Kondhor", "age": 22},
    {"name": "Donsten", "age": 17},
    {"name": "Tomus", "age": 20},
]
sorted_people = sorted(people, key=lambda x: x["name"])
for human in sorted_people:
    print(human)

from operator import itemgetter

people = [
    {"name": "Kondhor", "age": 22},
    {"name": "Donsten", "age": 17},
    {"name": "Tomus", "age": 20},
]
sorted_people = sorted(people, key=itemgetter("age"))
for human in sorted_people:
    print(human)

# 4) Store unique values with Sets

my_list = [1, 2, 3, 4, 5, 6, 3, 2, 3, 4, 2]
my_set = set(my_list)
print(my_set)

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
print(primes)

# 5) Save memory with Generators


a_list = [i for i in range(1000000)]
print(sum(a_list))
print(sys.getsizeof(a_list) / 1024, "kilobytes")
#
a_gen = (i for i in range(100000000))
print(sum(a_gen))
print(sys.getsizeof(a_gen) / 1024, "kilobytes")
#
b_gen = iter(range(100000000))
print(sum(b_gen))
print(sys.getsizeof(b_gen) / 1024, "kilobytes")

# 6) Define default values in Dictionaries with .get() and .setdefault()

# wrong way
my_dict = {"item": "macbook", "price": 1000}
count = my_dict["count"]
print(count)
# right way
my_dict = {"item": "macbook", "price": 1000}
count = my_dict.get("count")
print(count)
# if 'count' does not exist, create it with specified value
count = my_dict.setdefault("count", 2)
print(count)
print(my_dict)

# 7) Count hashable objects with collections.Counter

from collections import Counter

c_list = [1, 3, 5, 2, 2, 3, 3, 4, 5, 6, 8, 9, 0, 8, 7, 6, 4, 5, 5, 4, 6, 7]
counter = Counter(c_list)
print(counter)
# count a specified item
print(counter[4])
# the most common item(s)
most_common = counter.most_common(3)
print(most_common)
# access the most common item w/o counting
print(most_common[0][0])

# 8) Format strings with f-Strings (Python 3.6+)

NAME = "Kondhor"
greet = f"Hello {NAME}"
print(greet, end="!\n")

i = int(input("Input a number: "))
print(f"{i} squared is {i**2}", end=None)

# 9) Concatenate strings with .join()

darkness = ["Hello", "darkness", "my", "old", "friend."]
# BAD way
MY_STR = ""
for i in darkness:
    MY_STR += i + " "
print(MY_STR)
print(sys.getsizeof(MY_STR), " bytes")
# RIGHT way
G_STRING = " ".join(darkness)
print(G_STRING)
print(sys.getsizeof(G_STRING), " bytes")
# or if you feel like it
M_STRING = "".join(i + " " for i in darkness)
print(M_STRING)
print(sys.getsizeof(M_STRING), " bytes")

# 10) Merge dictionaries with {**d1, **d2} (Python 3.5+)

person1 = {"name": "Kondhor", "age": 25}
person2 = {"name": "Kondhor", "city": "Buenos Aires"}
merged_person = {**person1, **person2}
print(merged_person)
print(sys.getsizeof(merged_person), "bytes")

# 11) Simplify if-statements with if x in list

colors = ["red", "green", "blue", "yellow"]
COLOR = "red"
# BAD
if COLOR == "red" or COLOR == "green" or COLOR == "blue" or COLOR == "yellow":
    print("It is probably what you think it is.")
# RIGHT
if COLOR in ("red", "green", "blue", "yellow"):
    print("It is probably what you think it is.")
