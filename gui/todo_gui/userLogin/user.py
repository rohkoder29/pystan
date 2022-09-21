import random as rd
import string

# class User(object):

#   """docstring for User"""

#   def __init__(self, username, password):
#     self.username = username
#     self.password = password

#     self.connected = False
#     self.attempts = 3

#   def login(self):
#     user_password = input('Enter your password: ')
#     if user_password == self.password:
#       self.connected = True
#       print('Successfully logged in.')
#     else:
#       self.attempts -= 1
#       if self.attempts:
#         print('Bad credentials. Please retry.')
#         print(f'Attempts left: {self.attempts}')
#         self.login()
#       else:
#         print('That\'s enough. Next time get your credentials right.')

#   def logout(self):
#     if self.connected:
#       self.connected = False
#       print('Successfully logged out.')

#   def __str__(self) -> str:
#     self.connected = 'active' if self.connected else 'inactive'
#     return f'My username is {self.username} and my session is {self.connected}.'

# pseudo = input('Enter your username: ')
# access = input('Enter your password: ')
# userA = User(username=pseudo, password=access)
# print(userA)
# userA.login()
# print(userA)
# userA.logout()

print(f"{''.join(map(str, rd.choices(string.ascii_uppercase, k=5)))}")
print(f"{''.join(rd.choices(string.ascii_uppercase, k=5))}")
