def vigenere_encrypt(plaintext, keyword):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    keyword = keyword.upper()

    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for p_char, k_char in zip(plaintext, keyword_repeated):
        p_index = alphabet.index(p_char)
        k_index = alphabet.index(k_char)

        # Шифрование с использованием формулы
        c_index = (p_index + k_index) % len(alphabet)
        ciphertext.append(alphabet[c_index])

    return ''.join(ciphertext)


if __name__ == "__main__":
    surname = "ЕПИФАНОВ"
    text = "ДЕНИСЕВГЕНЬЕВИЧ5.py"
    encrypted_text = vigenere_encrypt(text, surname)
    print(f'Зашифрованный текст: {encrypted_text}')
