# https://math.libretexts.org/Bookshelves/Applied_Mathematics/Math_in_Society_(Lippman)/16%3A_Cryptography/16.03%3A_Transposition_Ciphers


import random


def encrypt(msg: str, key: str) -> str:
    key = len(key) # cogitar trocar a key pra int
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





def brute_force_attack(cipher_text: str) -> int:
    # testa todas as possibilidades de tamanho de senha até o tamanho do texto
    key_attempt = "a"
    while len(key_attempt) < len(cipher_text):
        attempt = decrypt(cipher_text, key_attempt)
        print(f"{len(key_attempt)}. {attempt}")
        key_attempt += "a"
    resp = int(input("Qual tentativa foi a correta? "))
    print(f"A chave é uma palavra de {resp} caracteres!")
    
    return resp


def freq_dist_attack(cipher_text: str) -> None:
    pass



def teste():
    C = encrypt("fujametranquemtodasasportasdeusestaconosco", "salvemse")
    print(C)
    print(decrypt(C, "salvemse"))
    brute_force_attack(C)

teste()