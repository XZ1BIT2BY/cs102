import random, string, vigenere
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    keyword = keyword.upper()  # Приводим ключевое слово к верхнему регистру для унификации

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            # Определяем, является ли символ буквой
            start = ord('A') if char.isupper() else ord('a')
            # Определяем начальный код для заглавных и строчных букв
            key_char = keyword[i % len(keyword)]  # Получаем символ ключа для текущей позиции
            key_shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')
            # Вычисляем сдвиг для символа ключа
            encrypted_char = chr((ord(char) - start + key_shift) % 26 + start)
            # Шифруем символ и добавляем его к результату
            ciphertext += encrypted_char
        else:
            # Оставляем символы, не являющиеся буквами, без изменений
            ciphertext += char


    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    keyword = keyword.upper()  # Приводим ключевое слово к верхнему регистру для унификации

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            # Определяем, является ли символ буквой
            start = ord('A') if char.isupper() else ord('a')
            # Определяем начальный код для заглавных и строчных букв
            key_char = keyword[i % len(keyword)]  # Получаем символ ключа для текущей позиции
            key_shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')
            # Вычисляем сдвиг для символа ключа
            decrypted_char = chr((ord(char) - start - key_shift) % 26 + start)
            # Дешифруем символ и добавляем его к результату
            plaintext += decrypted_char
        else:
            # Оставляем символы, не являющиеся буквами, без изменений
            plaintext += char



    return plaintext

