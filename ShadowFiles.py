import hashlib
import base64

iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
#salt = "".encode()
validation = "SALTED-SHA512-PBKDF2"

password = "password".encode()

# Alice value
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
entropy = base64.b64encode(value)
print("Alice: ", validation, iterations, entropy)

# Bob value
salt = base64.b64decode("6VuJKkHVTdDelbL7kVAI=".encode())
password = "password".encode()
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
entropy = base64.b64encode(value)
print("Bob: ", validation, iterations, entropy)

