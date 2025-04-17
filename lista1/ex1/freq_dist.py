from ..utils import timer
from .enc_dec import decrypt

chars_freq = {
    'a': 13.9, 'b': 1.0, 'c': 4.4, 'd': 5.4, 'e': 12.2,
    'f': 1.0, 'g': 1.2, 'h': 0.8, 'i': 6.9, 'j': 0.4,
    'k': 0.1, 'l': 2.8, 'm': 4.2, 'n': 5.3, 'o': 10.8,
    'p': 2.9, 'q': 0.9, 'r': 6.9, 's': 7.9, 't': 4.9,
    'u': 4.0, 'v': 1.3, 'w': 0.0, 'x': 0.3, 'y': 0.0, 'z': 0.4
}


@timer
def freq_dist_attack(cipher_text: str, testing: bool=False):
    cipher_text = cipher_text.lower()
    alphabet_lenght = 26
    freq = {}
    for char in cipher_text:
        if freq.get(char):
            freq[char] += 1
        else:
            freq[char] = 1
    total = sum(freq.values())
    freq_dist = {char: (count / total) * 100 for char, count in freq.items()}
    sorted_freq = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)
    print(f"\nFrequência dos caracteres no texto cifrado:\n{sorted_freq}\n")
    sorted_portuguese_freq = sorted(chars_freq.items(), key=lambda x: x[1], reverse=True)
    best_guesses = []
    for i in range(3):
        for j in range(3):
            guess = (ord(sorted_freq[i][0]) - ord(sorted_portuguese_freq[j][0]))%alphabet_lenght
            if guess not in best_guesses:
                best_guesses.append(guess)

    ind = 1
    attempts = []
    for guess in best_guesses:
        attempt = decrypt(cipher_text, guess)
        print(f"{ind}. Tentativa: {attempt}")
        attempts.append(attempt)
        ind += 1
    if not testing:
        resp = int(input("Qual tentativa foi a correta? "))
        print(f"A chave é {best_guesses[resp-1]}!")
        print("É a cifra de César!") if best_guesses[resp-1]==3 else None
        return best_guesses[resp-1]

    return attempts


# Testes de encriptação e decriptação

# Exemplo 1
# msg = "meunomeeguilherme"
# key = 1
# cipher_text = encrypt(msg, key)
# print(f"\nEncriptando \"{msg}\" com chave {key}: {cipher_text}\n")

# print(f"\nDecriptando \"{cipher_text}\" com chave {key}: {decrypt(cipher_text, key)}\n")

# # Exemplo 2
# msg = "zezeviuazebra"
# key = 3
# cipher_text = encrypt(msg, key)
# print(f"\nEncriptando \"{msg}\" com chave {key}: {cipher_text}\n")

# print(f"\nDecriptando \"{cipher_text}\" com chave {key}: {decrypt(cipher_text, key)}\n")


# # Testes de brute force

# # Exemplo 1
# key = brute_force_attack("chchylxdcheud") # zezeviuazebra
# print(f"{key}\n")

# # Exemplo 2
# # Esse exemplo usa o argumento testing=True para calcular o tempo de execução corretamente
# brute_force_attack("pajcdhktgxuxfjtbphcdiphsphegdkphstkdrth", testing=True) # alunosverifiquemasnotasdasprovasdevoces

# # Testes de frequência

# # Exemplo 1
# key = freq_dist_attack("chchylxdcheud") # zezeviuazebra
# print(f"{key}\n")

# # Exemplo 2
# # Esse exemplo usa o argumento testing=True para calcular o tempo de execução corretamente
# freq_dist_attack("pajcdhktgxuxfjtbphcdiphsphegdkphstkdrth", testing=True) # alunosverifiquemasnotasdasprovasdevoces

key = freq_dist_attack("rodwxgrehp")
print(key)