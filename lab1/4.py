def char_to_num(char):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return alphabet.index(char)


def num_to_char(num):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return alphabet[num]


def hill_cipher_encrypt(text, key_matrix):
    nums = [char_to_num(char) for char in text]

    while len(nums) % 3 != 0:
        nums.append(char_to_num('А'))  # Добавляем 'А' (0) для дополнения

    encrypted_nums = []
    for i in range(0, len(nums), 3):
        block = nums[i:i + 3]
        # Умножаем блок на матрицу ключа
        encrypted_block = [
            (key_matrix[0][0] * block[0] + key_matrix[0][1] * block[1] + key_matrix[0][2] * block[2]) % 32,
            (key_matrix[1][0] * block[0] + key_matrix[1][1] * block[1] + key_matrix[1][2] * block[2]) % 32,
            (key_matrix[2][0] * block[0] + key_matrix[2][1] * block[1] + key_matrix[2][2] * block[2]) % 32
        ]
        encrypted_nums.extend(encrypted_block)

    encrypted_text = ''.join(num_to_char(num) for num in encrypted_nums)
    return encrypted_text


if __name__ == "__main__":
    K = [[4, 18, 15],
         [10, 11, 19],
         [32, 5, 23]]
    text = "ЕПИФАНОВДЕНИСЕВГЕНЬЕВИЧ"
    encrypted_text = hill_cipher_encrypt(text, K)
    print(f'Зашифрованный текст: {encrypted_text}')
