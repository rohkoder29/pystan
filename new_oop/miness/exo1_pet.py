#!/usr/bin/env python3

'''

'''

# import

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

class Pet:
    def __init__(self) -> None:
        self.__name = ""   # an attribute with a leading dunder
        self.__type = ""   # is called a hidden/private attribute
        self.__age = 0     # no one outside the class context can see it

    # mutator methods (setter)
    def setName(self, name) -> None:
        self.__name = name.title()

    def setType(self, type) -> None:
        self.__type = type

    def setAge(self, age) -> None:
        self.__age = age

    # accessor methods (getter)
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type.title()

    def getAge(self):
        return self.__age

    # data output format
    def __str__(self) -> str:
        return f'{self.__name} is a {self.__age} year-old {self.__type}.'


def main() -> None:
    '''  '''
    # creating an instance of the Pet class
    pet_x = Pet()
    print(pet_x)    # as of now it should output the default values
    # 
    pet_1 = Pet()
    while True:
        try:
            name = input("Input pet name: ")
            assert len(name) >= 1
        except AssertionError:
            print("Name must contain at least one (1) character.")
        else:
            pet_1.setName(name)
            break
    while True:
        try:
            _type = input("Input pet type: ")
            assert len(_type) >= 1
            assert _type.isalpha()
        except AssertionError:
            print("Please input a valid type.")
        else:
            pet_1.setType(_type)
            break

    while True:
        try:
            age = int(input("Input pet age: "))
            assert age >= 0
        except ValueError as e:
            print("Please input a valid number.")
        except AssertionError:
            print("Please input a valid age.")
        else:
            pet_1.setAge(age)
            break

    print()
    print(f'Pet name: {pet_1.getName()}\nPet type: {pet_1.getType()}\nPet age: {pet_1.getAge()}')
    print()
    print(pet_1)
    

if __name__ == '__main__':
    '''  '''
    main()
