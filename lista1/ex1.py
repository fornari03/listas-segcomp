# ARQUIVO PARA EXERCICIO 1
# QUEBRANDO SHIFT CIPHER

from utils import timer

chars_freq = {
    'a': 13.9, 'b': 1.0, 'c': 4.4, 'd': 5.4, 'e': 12.2,
    'f': 1.0, 'g': 1.2, 'h': 0.8, 'i': 6.9, 'j': 0.4,
    'k': 0.1, 'l': 2.8, 'm': 4.2, 'n': 5.3, 'o': 10.8,
    'p': 2.9, 'q': 0.9, 'r': 6.9, 's': 7.9, 't': 4.9,
    'u': 4.0, 'v': 1.3, 'w': 0.0, 'x': 0.3, 'y': 0.0, 'z': 0.4
}

def encrypt(msg: str, key: int) -> str:
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_lenght = 26
    cipher_text = ""
    for m in msg:
        if m in alphabet_lower:
            cipher_text += alphabet_lower[(alphabet_lower.find(m)+key)%alphabet_lenght]
        elif m in alphabet_upper:
            cipher_text += alphabet_upper[(alphabet_upper.find(m)+key)%alphabet_lenght]

    return cipher_text


def decrypt(cipher_text: str, key: int) -> str:
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_lenght = 26
    msg = ""
    for c in cipher_text:
        if c in alphabet_lower:
            msg += alphabet_lower[(alphabet_lower.find(c)-key)%alphabet_lenght]
        elif c in alphabet_upper:
            msg += alphabet_upper[(alphabet_upper.find(c)-key)%alphabet_lenght]

    return msg




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
    print(sorted_freq)
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


# TESTES

# Testes de encriptação e decriptação

# Exemplo 1
msg = "meunomeeguilherme"
key = 1
cipher_text = encrypt(msg, key)
print(f"Encriptando \"{msg}\" com chave {key}: {cipher_text}")

print(f"Decriptando \"{cipher_text}\" com chave {key}: {decrypt(cipher_text, key)}")

# Exemplo 2
msg = "zezeviuazebra"
key = 3
cipher_text = encrypt(msg, key)
print(f"Encriptando \"{msg}\" com chave {key}: {cipher_text}")

print(f"Decriptando \"{cipher_text}\" com chave {key}: {decrypt(cipher_text, key)}")


# Testes de brute force

# Exemplo 1
key = brute_force_attack("rodwxgrehp") # olatudobem
print(key)

# Exemplo 2


# Testes de frequência

# freq_dist_attack("irprvghvfrehuwrvvhhvfrqgdphvdoyhpvh") # fomosdescobertosseescondamesalvemse 
# freq_dist_attack("txdqgrvxujhrdoylyhughlpsrqhqwhqrjudpdgrhptxhdoxwdrdjxdugdvdehehprtxhyhpshodiuhqwhtxhdgxuhcdgrsuholrqdrwdugd") # quandosurgeoalviverdeimponentenogramadoemquealutaoaguardasabebemoquevempelafrentequeadurezadoprelionaotarda
# freq_dist_attack("doxqrvyhuliltxhpdvqrwdvgdvsurydvghyrfhv") # alunosverifiquemasnotasdasprovasdevoces
#print("zezeviuazebra" in freq_dist_attack("chchylxdcheud", testing=True)) #zezeviuazebra