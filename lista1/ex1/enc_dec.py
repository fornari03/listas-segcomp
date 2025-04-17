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