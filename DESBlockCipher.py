from pyDes import *

message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

cipher = k.encrypt(message)
print("Length of plain text: ", len(message))
print("Length of cipher text: ", len(cipher))
print("Encrypted: ", cipher[0:8])
print("Encrypted: ", cipher[8:16])
print("Encrypted: ", cipher[16:])

message = k.decrypt(cipher)
print("Decrypted: ", message)