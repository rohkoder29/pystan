from cryptography.fernet import Fernet

# create the key
key = Fernet.generate_key()

# write it to a .key file
encryption_key = input("Input file to store the encryption key [with no extension]: ")
with open(f"{encryption_key}.key", "wb") as filekey:
    filekey.write(key)

# open the .key file created above to read the key
with open(f"{encryption_key}.key", "rb") as filekey:
    key = filekey.read()
 
# pass the key to the Fernet object
fernet = Fernet(key)
 
# open the file to encrypt
# read and save its data into a variable
file_to_encrypt = input("Input the file you want to encrypt: ")
with open(file_to_encrypt, 'rb') as file:
    original_data = file.read()
 
# encrypt the data
encrypted_data = fernet.encrypt(original_data)

# write the encrypted data back to a new file
new_encrypted_file = input("Input name for the new encrypted file: ")
with open(new_encrypted_file, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

print("Yay! File successfully encrypted!")

