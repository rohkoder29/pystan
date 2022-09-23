##################################
# SOME TIPS AND TRICKS IN PYTHON #
##################################

### Most frequent value of a list

from random import randint

somelist = [randint(0, 10) for a in range(randint(5, 20))]
print(f"Values in the list: {somelist}")

# non efficient way
current_max = 0
current_value = None

for x in somelist:
    if somelist.count(x) > current_max:
        current_max = somelist.count(x)
        current_value = x

print(f"Most frequent value: {current_value}, occurs {current_max} times.")

# more efficient way
# using `Counter` class from the `collections` module
# it comes with a builtin `most_common()` method which we will use

from collections import Counter

# create a Counter instance (object) on the list
counter = Counter(somelist)

current_max = counter.most_common()[0]
# by default this returns the 10 first most frequent value(s)
# in a list of tuples formatted like [(value, count)...]
# we can extract it using slicing or by passing an argument right
# into the method to specify how many most frequent values we want
# which in our case is 1
current_max = counter.most_common(1)[0]

print(f"Most frequent value: {current_value}, occurs {current_max[1]} times.")

# one other method is to use the `max()` function

# by default it looks for the largest value but we can pass
# a parameter to shift its behaviour a bit

print(max(somelist, key=somelist.count))
# this will print the most frequent value in our list

# we can do it more efficiently by transforming our list into a set
# which will delete the duplicated numbers
most_freq = max(set(somelist), key=somelist.count)
freq = somelist.count(most_freq)

print(f"Most frequent value: {most_freq}, occurs {freq} times.")

