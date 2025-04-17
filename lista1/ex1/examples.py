from .enc_dec import encrypt, decrypt
from .brute_force import brute_force_attack
from .freq_dist import freq_dist_attack



# Exemplos de encriptação e decriptação

# Exemplo 1
def enc_dec_1():
    msg = "meunomeeguilherme"
    key = 1
    cipher_text = encrypt(msg, key)
    print(f"\nEncriptando \"{msg}\" com chave {key}: {cipher_text}\n")

    print(f"\nDecriptando \"{cipher_text}\" com chave {key}: {decrypt(cipher_text, key)}\n")

# Exemplo 2
def enc_dec_2():
    msg = "zezeviuazebra"
    key = 3
    cipher_text = encrypt(msg, key)
    print(f"\nEncriptando \"{msg}\" com chave {key}: {cipher_text}\n")

    print(f"\nDecriptando \"{cipher_text}\" com chave {key}: {decrypt(cipher_text, key)}\n")


# Exemplos de brute force

# Exemplo 1
def brute_force_1():
    key = brute_force_attack("chchylxdcheud") # zezeviuazebra
    print(f"{key}\n")

# Exemplo 2
# Esse exemplo usa o argumento testing=True para calcular o tempo de execução corretamente
def brute_force_2():
    brute_force_attack("pajcdhktgxuxfjtbphcdiphsphegdkphstkdrth", testing=True) # alunosverifiquemasnotasdasprovasdevoces

# Testes de frequência

# Exemplo 1
def freq_dist_1():
    key = freq_dist_attack("chchylxdcheud") # zezeviuazebra
    print(f"{key}\n")

# Exemplo 2
# Esse exemplo usa o argumento testing=True para calcular o tempo de execução corretamente
def freq_dist_2():
    freq_dist_attack("pajcdhktgxuxfjtbphcdiphsphegdkphstkdrth", testing=True) # alunosverifiquemasnotasdasprovasdevoces

key = freq_dist_attack("rodwxgrehp")
print(key)


def menu():
    while True:
        exemplos = [enc_dec_1, enc_dec_2, brute_force_1, brute_force_2, freq_dist_1, freq_dist_2]
        print("0. Fechar programa")
        print("1. Exemplo 1 de encriptação/decriptação")

        print("Qualquer outro número significa criar um novo exemplo.")
        ex = input("Qual dos exemplos você quer rodar? ")
        if 0 <= ex <= 6:
            pass
        else:
            print("1. Encriptação")
            print("2. Decriptação")

            tipo = input("Qual exemplo você quer criar?")




menu()