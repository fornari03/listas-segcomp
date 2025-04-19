from utils import timer
from enc_dec import decrypt

@timer
def brute_force_attack(cipher_text: str, testing: bool=False) -> int:
    text_len = len(cipher_text)
    # testa todos os divisores do tamanho do texto, já que o tamanho da chave é um divisor
    key_attempts = [i for i in range(1, text_len+1) if text_len % i == 0]
    ind = 1
    for attempt in key_attempts:
        attempt = decrypt(cipher_text, "a"*attempt)
        print(f"{ind}. {attempt}")
        ind += 1
    if not testing:
        resp = int(input("Qual tentativa foi a correta? "))
        print(f"A chave é uma palavra de {key_attempts[resp-1]} caracteres!")
        return key_attempts[resp-1]

    return 0