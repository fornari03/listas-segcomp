import random

def encrypt(msg: str, key: str) -> str:
    key = len(key)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_list = []
    cipher_text = ""
    i = 0
    while i < len(msg):
        if len(msg) - i >= key:
            cipher_list.append(msg[i:i + key])
        else:
            cipher_list.append(msg[i:])
            while len(cipher_list[-1]) < key:
                cipher_list[-1] += random.choice(alphabet)
        i += key

    print(cipher_list)
        
    for i in range(key):
        for j in range(len(cipher_list)):
            if i < len(cipher_list[j]):
                cipher_text += cipher_list[j][i]

    return cipher_text



def decrypt(cipher_text: str, key: str) -> str:
    key = len(key)
    msg = ""
    jump = len(cipher_text) // key
    i = 0
    while len(msg) < len(cipher_text):
        msg += cipher_text[i]
        i += jump
        if i >= len(cipher_text):
            i = i % len(cipher_text) + 1
    
    return msg