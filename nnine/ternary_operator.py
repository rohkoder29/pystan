##################################
# SOME TIPS AND TRICKS IN PYTHON #
##################################


# The ternary operator
""" It is used to make if statements more consise. """


# say we have this little program

while True:
    try:
        age = input("Please input your age: ")
        assert age.isdigit()
    except AssertionError:
        print("Please enter a valid number.")
    else:
        age = int(age)
        break

if age >= 18:
    print("You can be a voter.")
else:
    print("You'll have to wait a few years.")

# we could achieve this more easily by using the ternary operator

adult = True if age >= 18 else False

if adult:
    print("You're an adult.")
else:
    print("You're not (yet) an adult.")

# and go even further by doing

print("You can legally drink." if adult else "You can't legally drink!")

# okay all that is kinda cool but what if I have multiple if statements?
# [Hold my keyboard son]

print("You're very old" if age > 70 else "You're quite old" if age > 50 else "You're fairly young" if age > 30 else "Who are you?")


