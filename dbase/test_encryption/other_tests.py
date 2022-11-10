### test hashlib
import hashlib

# md5 = hashlib.md5()
# sha1 = hashlib.sha1()
# sha224 = hashlib.sha224()
# sha256 = hashlib.sha256()
# sha384 = hashlib.sha384()
# sha512 = hashlib.sha512()

# list_hash = [md5, sha1, sha224, sha256, sha384, sha512]
# file_to_hash = r"savory.key"

# with open(file_to_hash, "rb") as stream:
#     content = stream.read()
#     for hash_function in list_hash:
#         hash_function.update(content)
#         print(f"{hash_function.name}: {hash_function.hexdigest()}")


print(hashlib.algorithms_guaranteed)

