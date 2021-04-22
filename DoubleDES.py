from pyDes import *
import random

def modify(cipher):
    mod = [0]*len(cipher)
    mod[8] = 1
    # mod[10] = ord(' ') ^ ord('$')
    # mod[11] = ord(' ') ^ ord('1')
    # mod[12] = ord(' ') ^ ord('0')
    # mod[13] = ord('$') ^ ord('0')
    # mod[14] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


message = "01234567"

key_11 = random.randrange(0, 256)
key_21 = random.randrange(0, 256)

key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])
key_2 = bytes([key_21, 0, 0, 0, 0, 0, 0, 0])

iv = bytes([0]*8)

k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)

cipher = k1.encrypt(k2.encrypt(message))

# Bob modifying the cipher text
# cipher = modify(cipher)
print("Key 11: ", key_11)
print("Key 21: ", key_21)
print("Encrypted: ", cipher)

# This is bob
message = k2.decrypt(k1.decrypt(cipher))
print("Decrypted: ", message)

# Eves attack on double des encrpytion
lookup = {}
for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    lookup[k.encrypt(message)] = i

for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    if k.decrypt(cipher) in lookup:
        print("Key 11", i)
        print("Key 21", lookup[k.decrypt(cipher)])
        key_1 = bytes([i, 0, 0, 0, 0, 0, 0, 0])
        key_2 = bytes([lookup[k.decrypt(cipher)], 0, 0, 0, 0, 0, 0, 0])
        k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
        k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)
        print("Eve breaking double DES: ", k2.decrypt(k1.decrypt(cipher)))
        break

# print("Length of plain text: ", len(message))
# print("Length of cipher text: ", len(cipher))
# print("Encrypted: ", cipher[0:8])
# print("Encrypted: ", cipher[8:16])
# print("Encrypted: ", cipher[16:])