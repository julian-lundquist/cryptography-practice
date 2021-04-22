from pyDes import *

def modify(cipher):
    mod = [0]*len(cipher)
    mod[9] = 1
    # mod[10] = ord(' ') ^ ord('$')
    # mod[11] = ord(' ') ^ ord('1')
    # mod[12] = ord(' ') ^ ord('0')
    # mod[13] = ord('$') ^ ord('0')
    # mod[14] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


message = "Give Bob:    10$ and send them to him"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

cipher = k.encrypt(message)
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Decrypted:", cipher)

# Bob modifying the cipher text
cipher = modify(cipher)

# this is the bank decrypting the message
message = k.decrypt(cipher)
print("Decrypted", message)