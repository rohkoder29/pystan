from cryptography.fernet import Fernet

# retrieve the key for decryption
encryption_key = input("Input the file containing the encryption key: ")
with open("file.key", "rb") as decrypt:
    key = decrypt.read()

# pass the key to the Fernet object
fernet = Fernet(key)

# open the file we want to decrypt to retrieve data
file_to_decrypt = input("Input the file yoo want to decrypt: ")
with open(file_to_decrypt, "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# decrypt the retrieved data
decrypted_data = fernet.decrypt(encrypted_data)

# append the decrypted data back to the file
with open(file_to_decrypt, "wb") as stream:
    stream.write(decrypted_data)

print("Yay! File successfully decrypted!")


