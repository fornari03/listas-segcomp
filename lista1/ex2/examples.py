from enc_dec import encrypt, decrypt
from brute_force import brute_force_attack
from freq_dist import freq_dist_attack



# Exemplos de encriptação e decriptação

# Exemplo 1
def enc_dec_1():
    msg = "meunomeeguilherme"
    key = "nome"
    cipher_text = encrypt(msg, key)
    print(f"\nEncriptando \"{msg}\" com chave {key}: {cipher_text}\n")

    print(f"\nDecriptando \"{cipher_text}\" com chave de tamanho {key}: {decrypt(cipher_text, key)}\n")

# Exemplo 2
def enc_dec_2():
    msg = "olatudobem"
    key = "oi"
    cipher_text = encrypt(msg, key)
    print(f"\nEncriptando \"{msg}\" com chave {key}: {cipher_text}\n")

    print(f"\nDecriptando \"{cipher_text}\" com chave de tamanho {key}: {decrypt(cipher_text, key)}\n")


# Exemplos de brute force

# Exemplo 1
def brute_force_1():
    key = brute_force_attack("eoaeaieouulismnrspmrsshl") # eusoupalmeirassimsenhor
    print(f"{key}\n")

# Exemplo 2
# Esse exemplo usa o argumento testing=True para calcular o tempo de execução corretamente
def brute_force_2():
    brute_force_attack("nimseaoacroqirlsuseheeeve", testing=True) # naoseioquemaisescrever

# Testes de frequência

# Exemplo 1
def freq_dist_1():
    key = freq_dist_attack("eoaeaieouulismnrspmrsshl") # eusoupalmeirassimsenhor
    print(f"{key}\n")

# Exemplo 2
# Esse exemplo usa o argumento testing=True para calcular o tempo de execução corretamente
def freq_dist_2():
    freq_dist_attack("nimseaoacroqirlsuseheeeve", testing=True) # naoseioquemaisescrever



def menu():
    while True:
        print("\n1. Exemplo 1 de encriptação/decriptação")
        print("2. Exemplo 2 de encriptação/decriptação")
        print("3. Exemplo 1 de brute force")
        print("4. Exemplo 2 de brute force (testing=True)")
        print("5. Exemplo 1 de teste de frequência")
        print("6. Exemplo 2 de teste de frequência (testing=True)")
        print("7. Criar novo exemplo de encriptação")
        print("8. Criar novo exemplo de decriptação")
        print("9. Criar novo exemplo de brute force")
        print("10. Criar novo exemplo de brute force (testing=True)")
        print("11. Criar novo exemplo de teste de frequência")
        print("12. Criar novo exemplo de teste de frequência (testing=True)")

        print("Qualquer outro número significa fechar o programa.\n")
        ex = input("Qual dos exemplos você quer rodar? ")
        if ex == "1":
            enc_dec_1()
        elif ex == "2":
            enc_dec_2()
        elif ex == "3":
            brute_force_1()
        elif ex == "4":
            brute_force_2()
        elif ex == "5":
            freq_dist_1()
        elif ex == "6":
            freq_dist_2()
        elif ex == "7":
            msg = input("Digite a mensagem que você quer encriptar: ")
            key = input("Digite a chave: ")
            cipher_text = encrypt(msg, key)
            print(f"\nEncriptando \"{msg}\" com chave {key}: {cipher_text}\n")
        elif ex == "8":
            cipher_text = input("Digite a mensagem que você quer decriptar: ")
            key = input("Digite a chave: ")
            print(f"\nDecriptando \"{cipher_text}\" com chave {key}: {decrypt(cipher_text, key)}\n")
        elif ex == "9":
            cipher_text = input("Digite a mensagem que você quer quebrar: ")
            key = brute_force_attack(cipher_text)
            print(f"\nA chave é: {key}\n")
        elif ex == "10":
            cipher_text = input("Digite a mensagem que você quer quebrar: ")
            brute_force_attack(cipher_text, testing=True)
        elif ex == "11":
            cipher_text = input("Digite a mensagem que você quer quebrar: ")
            key = freq_dist_attack(cipher_text)
            print(f"\nA chave é: {key}\n")
        elif ex == "12":
            cipher_text = input("Digite a mensagem que você quer quebrar: ")
            freq_dist_attack(cipher_text, testing=True)
        else:
            print("Fechando o programa.")
            break

menu()