import hashlib
import base64

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

# Alice and Bob share a secret key
secret_key = "secret key".encode()

# Alice wants to compute a MAC
m = "Hey Bob, you are still awesome.".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = base64.b64encode(sha256.digest())

print(m, hmac)

# Eve modifying the message maliciously
m = modify(m)
print(m)

# Bob receives and validates the HMAC
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = base64.b64encode(sha256.digest())

print(m, hmac)