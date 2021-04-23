import hashlib
import base64

def guess_password(salt, iterations, entropy):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c1 in alphabet:
        for c2 in alphabet:
            password = (c1 + c2).encode()
            value = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128))
            if value.decode() == entropy:
                return password
    return "".encode()

iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
#salt = "".encode()
validation = "SALTED-SHA512-PBKDF2"

password = "pw".encode()

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

entropy = "Kp64cWBoPly+4a+X6sIocmsYGM51a06+oNUaXR+avGHvIp8HzrArgsM5DTRQDppoeeaU59SJHZq7SYPESsXVIpAlXt5M4+bIfgYvg0Imu9mHBA4DDV7hnYFr3z/3iWgs6pKT1uMESDXZaBah1tZykKsZEWczAHwZ4irW4mexmJs="
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
password = guess_password(salt, iterations, entropy)
print(password)
value = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128))
print(value.decode())
print(entropy)

