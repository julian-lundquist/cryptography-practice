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

def modification(cipher):
    mod = [0] * len(cipher)
    mod[10] = ord(' ') ^ ord('$')
    mod[11] = ord(' ') ^ ord('1')
    mod[12] = ord(' ') ^ ord('0')
    mod[13] = ord('$') ^ ord('0')
    mod[14] = ord('1') ^ ord('0')

    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

# can change the key value by inputing in the parameters in KeyStream
key = KeyStream(10)
message = "Send Bob:    $10".encode()
cipher = encrypt(key, message)
print(cipher)
print(message)

# cipher = trasmit(cipher, 5)
# print(cipher)

# this is where the attacker functionallity is
cipher = modification(cipher)

key = KeyStream(10)
message = encrypt(key, cipher)
print(message)