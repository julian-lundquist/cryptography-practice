import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256

def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def trasmit(cipher, chance):
    b = []
    for c in cipher:
        if random.randrange(0, chance) == 0:
            c = c ^ 2**random.randrange(0, 8)
        b.append(c)
    return bytes(b)

# can change the key value by inputing in the parameters in KeyStream
key = KeyStream(10)
message = "Hello, World!".encode()
cipher = encrypt(key, message)
print(cipher)

cipher = trasmit(cipher, 5)
print(cipher)

key = KeyStream(10)
message = encrypt(key, cipher)

print(message)