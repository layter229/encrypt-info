def zigzag_encrypt(text):
    # Убираем пробелы и переводим текст в верхний регистр
    text = text.replace(" ", "").upper()

    # Создаем массив для уровней
    levels = [['' for _ in range(len(text))] for _ in range(2)]

    # Переменные для направления записи
    direction = 1  # 1 - вниз, -1 - вверх
    current_level = 0
    index = 0

    # Записываем текст по уровням
    for char in text:
        levels[current_level][index] = char

        # Меняем направление, если достигли верхнего или нижнего уровня
        if current_level == 0:
            direction = 1
        elif current_level == 2 - 1:
            direction = -1

        # Переход к следующему уровню
        current_level += direction

        # Увеличиваем индекс, если находимся на верхнем или нижнем уровне
        if direction == 1 and current_level == 2 - 1:
            index += 1
        elif direction == -1 and current_level == 0:
            index += 1

    # Преобразуем уровни в строки и создаем зашифрованный текст
    encrypted_text = [''.join(level) for level in levels]

    return levels, encrypted_text


if __name__ == "__main__":
    text = "ЕпифановДенисЕвгеньевич"  # ФамилияИмяОтчество
    levels_array, encrypted_text_array = zigzag_encrypt(text)
    print("Массив уровней:")
    for level in levels_array:
        print(level)
    print(f"Зашифрованное сообщение: {encrypted_text_array}")