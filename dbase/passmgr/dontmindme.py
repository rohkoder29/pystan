# try:
#     age = int(input("Your age: "))
#     raise Exception("Age entered.")
# except ValueError:
#     print("Age is incorrect.")
# else:
#     print("Hell yeah!")

import secrets
import uuid
from Crypto.Random import get_random_bytes as grb

#print(help(uuid))

#x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')
#salt = x.bytes
salt = grb(32)[:16]
print(salt)
print(uuid.UUID(bytes=salt))
