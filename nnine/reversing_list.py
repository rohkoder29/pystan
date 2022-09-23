##################################
# SOME TIPS AND TRICKS IN PYTHON #
##################################


# How do you reverse a list?
from random import randint
numbers = [randint(1, 20) for _ in range(randint(5, 10))]

# non efficient way
reverlist = []
for index in range(len(numbers)):
    reverlist.append(numbers[len(numbers) - index - 1])

print(numbers)
print(reverlist)

# fairly efficient using builtin reversed() and reverse() methods
reverlist_ = reversed(numbers)
# this one creates a reverseiterartor object
# but does not alter the original list
print(list(reverlist_))

numbers.reverse()
# note this reverses the list in-place
# meaning it replaces the original list
print(numbers)

# using index slicing
reverlist__ = reverlist[::-1]
print(reverlist__)


