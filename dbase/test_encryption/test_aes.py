######################################
# THIS IS A TEST OF THE AES PROTOCOL #
#   USING THE PYCRYPTODOME MODULE    #
######################################
#ft. n9

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2 #brute-force protection
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from cryptography.fernet import Fernet
from decrypt_file import Decrypt


# first we wanna create an en/decryption key
# aka symetric encrytion which means the same key
# is being used for both encryption and decryption

## generate a simple key to create our salt
#simple_key = get_random_bytes(32)
### after that we will no longer need it
#print(simple_key)
#### we'll save it in a file for the sake of security
salt_file = "savory.key"
#with open(salt_file, "wb") as stream:
#    stream.write(simple_key)

#### so the salt for our encryption is gonna be that
with open(salt_file, "rb") as stream:
    salt = stream.read()
#print(salt)

# the password for the key generation
## our password is stored in an encrypted file so we'll have to retrieve it
encryption_key_file = "passkey.key"
blind_password_file = "blind_password.txt"
### instanciate the Decrypt object
blind_file = Decrypt()
### instanciate the Fernet object
fernet = Fernet(blind_file.get_encryption_key(encryption_key_file))
### decrypt the file
decrypted_data = fernet.decrypt(blind_file.get_encrypted_data(blind_password_file))
password = decrypted_data.decode("UTF-8").strip()
# now that we have our salt and password, 
# we can go on and generate the actual encryption key

secure_key = PBKDF2(password, salt, dkLen=32)
#print(secure_key)

## we're gonna use this secure key in a cipher
## to encrypt a simple message

text = b"I know who actually pulled the trigger in the JFK thing..."

cipher = AES.new(secure_key, AES.MODE_CBC)
ciphered_text = cipher.encrypt(pad(text, AES.block_size))
print(ciphered_text)
# now the encryption is done

# what we could do now is export this ciphered data to a binary file

bin_file = "theTruthAboutJFK.bin"
with open(bin_file, "wb") as stream:
    stream.write(cipher.iv)
    stream.write(ciphered_text)

# at this point we have a .bin file containing our secret message

# we may also want to decrypt it
with open(bin_file, "rb") as stream:
    ## save the first 16 bits of data in the iv variable
    ## we use this to actually make the decryption
    iv = stream.read(16)
    encrypted_data = stream.read()

dec_cipher = AES.new(secure_key, AES.MODE_CBC, iv=iv)
dec_text = unpad(dec_cipher.decrypt(encrypted_data), AES.block_size)
print(dec_text.decode("UTF-8"))



