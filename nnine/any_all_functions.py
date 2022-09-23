#################################
# SOME TIPS AND TRICK IN PYTHON #
#################################

""" Very useful for checking content of iterables. """

### `any()` function
""" Returns True if at least one (1) element of the provided iterable is True. Returns False if the iterable is empty. """

#
a = [True, True, False, True, False]
print(any(a))
# this returns True because at least one (1) element in the list is True
b = [False, False, False, True]
print(any(b))
# this also returns True



### `all()` function
""" Returns True if all elements of the provided iterable is True. Also returns True if the iterable is empty. """

print(all(a))
# this returns False because at least one (1) element in the list is not True

c = []
print(all(c))
# this returns True because the list is empty

#########

# now imagine we have a bunch of random numbers...

from random import randint

numbers = [randint(1, 100) for _ in range(randint(1, 20))]
print(numbers)

# and some lambda to check for evenness
even = lambda x: x % 2 == 0

# so to check that out
result = [even(number) for number in numbers]

if any(result):
    print("At least one (1) number is even.")
else:
    print("No number is even here. It's odd land.")

if all(result):
    print("All numbers are even!")



