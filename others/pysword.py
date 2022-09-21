import secrets, string

# returns all ASCII 26 characters of the alphabet
# in both UPPER and lower case [aA-zZ]
letters = string.ascii_letters

# returns all ASCII decimal digits [0-9]
numbers = string.digits

# returns all ASCII punctuation characters
# [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]
symbols = string.punctuation

random_letter = secrets.choice(letters)
random_number = secrets.choice(numbers)
random_symbol = secrets.choice(symbols)

print(symbols)
