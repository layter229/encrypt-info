def zigzag_encrypt(text):
    text = text.replace(" ", "").upper()

    levels = [['' for _ in range(len(text))] for _ in range(2)]

    direction = 1
    current_level = 0
    index = 0

    for char in text:
        levels[current_level][index] = char

        if current_level == 0:
            direction = 1
        elif current_level == 2 - 1:
            direction = -1

        current_level += direction

        if direction == 1 and current_level == 2 - 1:
            index += 1
        elif direction == -1 and current_level == 0:
            index += 1

    encrypted_text = [''.join(level) for level in levels]

    return levels, encrypted_text


if __name__ == "__main__":
    text = "ЕпифановДенисЕвгеньевич"
    levels_array, encrypted_text_array = zigzag_encrypt(text)
    print("Массив уровней:")
    for level in levels_array:
        print(level)
    print(f"Зашифрованное сообщение: {encrypted_text_array}")