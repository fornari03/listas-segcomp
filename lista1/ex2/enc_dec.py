import random

def encrypt(msg: str, key: str) -> str:
    key = len(key)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_list = []
    cipher_text = ""
    i = 0
    while i < len(msg):
        if len(msg) - i >= key:
            # adiciona o bloco de tamanho key
            cipher_list.append(msg[i:i + key])
        else:
            # adiciona o último bloco com padding
            cipher_list.append(msg[i:])
            while len(cipher_list[-1]) < key:
                cipher_list[-1] += random.choice(alphabet)
        i += key

    print(f"Blocos formados pelo tamanho da chave: {cipher_list}")
        
    # forma a cifra a partir dos blocos
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
            # se o índice ultrapassa o tamanho do texto cifrado, reinicia
            i = i % len(cipher_text) + 1
    
    return msg