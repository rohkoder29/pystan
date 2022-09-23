##################################
# SOME TIPS AND TRICKS IN PYTHON #
##################################


# The lambda function

# let's say we have this function
def square(x):
    return x * x

print(square(2))

# we could make things a little more easy by using a lambda
square = lambda x: x * x
print(square(5))

# so a lambda is kinda a quick way to define a fairly simple function (called anonymous function)

# but of course we can spice things a little bit
# say passing multiple parameters
sum_ = lambda x, y: x + y
print(sum_(3, 6))

# unlimited parameters
string_ = lambda *args: " ".join(args)
print(string_("hello", "world", "from", "my", "couch"))


# another thing we can do is to not save the expression in a avariable by calling it directly in a print for example

print((lambda x: pow(x, 3))(3))
# but beware of the syntax difference

############

# the most popular use case for lambda expressions is to call it inside another (bigger) function
# since generally lambdas are used to do just one single operation

from random import randint

numbers = [randint(1, 100) for _ in range(randint(5, 15))]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(numbers, even_numbers)

squared_numbers = list(map(lambda x: pow(x, 2), even_numbers))
print(squared_numbers)

###########
# we can also return a lambda from a regular function

def loan(amount):
    return lambda x: x * amount

interest = loan(2_000)
print(interest(.1))

