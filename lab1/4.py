# Алфавит (русский, можно изменить на латиницу при необходимости)
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

plaintext = "денисевгеньевич"
key = "епифанов"

# Функция шифрования
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    auto_key = key + plaintext
     # Генерация ключа с автоматическим выбором
    key_indices = [alphabet.index(k) for k in auto_key[:len(plaintext)]]

    for i, char in enumerate(plaintext):
        if char in alphabet:
            text_index = alphabet.index(char)
            key_index = key_indices[i]
            encrypted_char = alphabet[(text_index + key_index) % len(alphabet)]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Если символ не в алфавите, просто добавляем его как есть

    return ''.join(encrypted_text)


encrypted = vigenere_encrypt(plaintext, key)


print(f"Оригинальный текст: {plaintext}")
print(f"Ключ: {key}")
print(f"Зашифрованный текст: {encrypted}")

