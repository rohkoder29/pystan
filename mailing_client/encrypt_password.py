from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("passkey.key", "wb") as passkey:
    passkey.write(key)

# opening the key
with open('passkey.key', 'rb') as passkey:
    key = passkey.read()
 
# using the generated key
fernet = Fernet(key)
 
# opening the original_password file to encrypt
with open('password.txt', 'rb') as file:
    original_password = file.read()
     
# encrypting the file
encrypted_password = fernet.encrypt(original_password)
 
# opening the file in write mode and
# writing the encrypted_password data
with open('password.txt', 'wb') as encrypted_password_file:
    encrypted_password_file.write(encrypted_password)
