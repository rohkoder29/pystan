from cryptography.fernet import Fernet

class Decrypt():
    def __init__(self) -> None:
        pass

    def get_encryption_key(self, encryption_key) -> bytes:
        # retrieve the key for decryption
        with open(encryption_key, "rb") as decrypt:
            key = decrypt.read()
        
        return key    

    def get_encrypted_data(self, file_to_decrypt) -> bytes:
        # open the file we want to decrypt to retrieve data
        with open(file_to_decrypt, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        return encrypted_data

    # def restore_decrypted_data(self, file_to_decrypt) -> None:
    #     # append the decrypted data back to a copy of the file
    #     with open(f"decrypted_{file_to_decrypt}", "wb") as stream:
    #         stream.write(decrypted_data)

    #     return None


# mister = Decrypt()

# # pass the key to the Fernet object
# encryption_key = input("Input the file containing the encryption key: ")
# fernet = Fernet(mister.get_encryption_key(encryption_key))

# # decrypt the retrieved data
# file_to_decrypt = input("Input the file yoo want to decrypt: ")
# decrypted_data = fernet.decrypt(mister.get_encrypted_data(file_to_decrypt))

# # restore decrypted data to a copy of the file
# mister.restore_decrypted_data(file_to_decrypt)

# print("Yay! File successfully decrypted!")


