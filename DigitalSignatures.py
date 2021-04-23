import hashlib
# These are Alice's keys
# Public Key (e,n): 7 123463
# Secret Key (d): 2923

n = 123463
e = 7
d = 2923

# This is the message that Alice wants to sign and send to Bob
message = "Bob you are awesome".encode()

# Step 1: hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash Value: ", h)

# Step 2: Decrypt the hash value (use secret exponent)
sign = h**d % n

# Step 3: Send message with signature to Bob
print(message, sign)

# This is Bob verifying the message signature and decrypting message
# Step 1: This is Bob verifying the message signature
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash Value: ", h)

# Step 2: Verify Message Signature
verification = sign**e % n
print("Verification Value: ", verification)