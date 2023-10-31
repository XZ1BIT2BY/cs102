def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Определяем начальный код для заглавных или строчных букв
            start = ord('A') if char.isupper() else ord('a')
            # Шифруем символ с учетом сдвига и добавляем его к результату
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += encrypted_char
        else:
            # Оставляем символы, не являющиеся буквами, без изменений
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Определяем начальный код для заглавных или строчных букв
            start = ord('A') if char.isupper() else ord('a')
            # Дешифруем символ с учетом сдвига и добавляем его к результату
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            plaintext += decrypted_char
        else:
            # Оставляем символы, не являющиеся буквами, без изменений
            plaintext += char
    return plaintext
