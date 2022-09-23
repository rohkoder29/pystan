##################################
# SOME TIPS AND TRICKS IN PYTHON #
##################################


### `map()` function
""" The sole purpose of this function is to 'map' a function to an iterable."""


from random import randint

numbers = [randint(0, 100) for _ in range(randint(0, 10))]
print(numbers)

square = lambda x: pow(x, 2)
new_numbers = [square(x) for x in numbers]
print(new_numbers)

# using the map function

new_numbers_map = map(square, numbers)
# this creates a <map> object

# to actually vizualise it we convert it into a list
print(list(new_numbers_map))


# we can also pass other builtins to that iterable
cast_to_str = map(str, numbers)
print(list(cast_to_str))

