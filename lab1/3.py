# Алфавит (русский, можно изменить на латиницу при необходимости)
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'




# Функция шифрования
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    key_indices = [alphabet.index(k) for k in key]

    for i, char in enumerate(plaintext):
        if char in alphabet:
            text_index = alphabet.index(char)
            key_index = key_indices[i % key_length]
            encrypted_char = alphabet[(text_index + key_index) % len(alphabet)]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


if __name__ == "__main__":
    plaintext = "денисевгеньевич"
    key = "епифанов"
    encrypted = vigenere_encrypt(plaintext, key)
    print(f"Зашифрованный текст: {encrypted}")
