@timer
def brute_force_attack(cipher_text: str, testing: bool=False) -> int:
    # testa todas as possibilidades de tamanho de senha até o tamanho do texto
    key_attempt = "a"
    while len(key_attempt) < len(cipher_text):
        attempt = decrypt(cipher_text, key_attempt)
        print(f"{len(key_attempt)}. {attempt}")
        key_attempt += "a"
    if not testing:
        resp = int(input("Qual tentativa foi a correta? "))
        print(f"A chave é uma palavra de {resp} caracteres!")
    
    return resp
