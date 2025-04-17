from utils import timer
from enc_dec import decrypt


@timer
def brute_force_attack(cipher_text: str, testing: bool=False) -> int:
    for i in range(26):
        attempt = decrypt(cipher_text, i)
        print(f"{i+1}. {attempt}")
    
    if not testing:
        resp = int(input("Qual tentativa foi a correta? "))
        print(f"A chave é {resp-1}!")
        print("É a cifra de César!") if resp==4 else None
        return resp-1
    return 0