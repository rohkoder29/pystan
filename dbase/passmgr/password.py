from getpass import getpass
import hashlib
# from Crypto.Random import get_random_bytes
from cryptography.fernet import Fernet
from os import urandom
from os import environ as env


class Password:
    def __init__(self) -> None:
        self._password = ""
        self._salt = ""
        self._hash = ""

    def validate_password_input(self) -> str:
        while True:
            try:
                self._password = getpass("Choose your password: ")
                assert len(self._password) >= 8
            except AssertionError:
                print("Password must be at least 8 characters.")
            else:
                break
        return self._password

    def create_salt(self) -> bytes:
        # self._salt = get_random_bytes(32)
        self._salt = hashlib.sha256(urandom(60)).hexdigest().encode('UTF-8')
        return self._salt
    
    def hash_password(self, salted_password) -> str:
        hash_ = hashlib.sha512()
        hash_.update(salted_password)
        return hash_.hexdigest()
    
    def encrypt_password(self, hashed_password) -> bytes:
        key = env.get("PM_PEPPER")
        fernet = Fernet(key.encode("UTF-8"))
        # currently skipping the encoding step
        # return fernet.encrypt(hashed_password.encode("UTF-8"))
        return fernet.encrypt(hashed_password)

    def decrypt_password(self, peppered_password) -> bytes:
        key = env.get("PM_PEPPER")
        fernet = Fernet(key.encode("UTF-8"))
        return fernet.decrypt(peppered_password.encode("UTF-8"))

    def unhash_password(self, hashed_password) -> None:
        pass
