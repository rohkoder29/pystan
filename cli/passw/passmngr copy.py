import os
import sys
import sqlite3
import secrets
import random
import string





print("\nWELCOME TO THE PASSWORD GENERATOR APP\n")

ALPHABET = list(string.ascii_letters)
NUMBERS = list(string.digits)
SYMBOLS = list("!@#~|$%&*?")


# # A Sample class with init method
# class Person:
   
#     # init method or constructor 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     # Sample Method 
#     def say_hi(self):
#         print(f'Hello, my name is {self.name.title()} and I\'m {self.age}.')


# def get_name():
#     return input("What's your name? ")

# def get_age():
#    return int(input("How old are you? "))

# p = Person(get_name(), get_age())
# p.say_hi()
