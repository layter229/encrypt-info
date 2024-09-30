import re

# Функция для создания таблицы шифра на основе ключевого слова (5x6)
def create_playfair_table(key):
    # Используем 30 символов: исключаем "ё", объединяем "и/й"
    alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюя"
    key = re.sub(r'[^а-я]', '',
                 key.lower().replace("ё", "е").replace("й", "и"))  # Очищаем ключ от недопустимых символов
    table = []
    used_letters = set()

    # Заполняем таблицу уникальными буквами из ключа
    for char in key:
        if char not in used_letters and char in alphabet:
            table.append(char)
            used_letters.add(char)

    # Добавляем оставшиеся буквы алфавита
    for char in alphabet:
        if char not in used_letters:
            table.append(char)

    # Преобразуем в таблицу 5x6
    table = [table[i:i + 6] for i in range(0, len(table), 6)]
    return table


# Функция для поиска координат символа в таблице
def find_position(table, char):
    for row in range(len(table)):
        if char in table[row]:
            return row, table[row].index(char)
    return None


# Функция для шифрования текста
def encrypt_playfair(plaintext, key):
    table = create_playfair_table(key)

    # Преобразуем входной текст, удаляем пробелы и заменяем "ё" на "е", "й" на "и"
    plaintext = re.sub(r'[^а-я]', '', plaintext.lower().replace("ё", "е").replace("й", "и"))

    # Обрабатываем текст по парам символов
    digraphs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
            if a == b:
                b = 'я' if a != 'я' else 'а'  # Если символы одинаковые, вставляем разделитель
            else:
                i += 1
        else:
            b = 'я'  # Если символ без пары, добавляем "я"
        digraphs.append((a, b))
        i += 1

    ciphertext = ''

    # Шифруем пары символов
    for a, b in digraphs:
        row_a, col_a = find_position(table, a)
        row_b, col_b = find_position(table, b)

        if row_a == row_b:
            # Если символы в одной строке, сдвигаем вправо
            ciphertext += table[row_a][(col_a + 1) % 6]
            ciphertext += table[row_b][(col_b + 1) % 6]
        elif col_a == col_b:
            # Если символы в одном столбце, сдвигаем вниз
            ciphertext += table[(row_a + 1) % 5][col_a]
            ciphertext += table[(row_b + 1) % 5][col_b]
        else:
            # Если символы находятся в разных строках и столбцах, меняем столбцы
            ciphertext += table[row_a][col_b]
            ciphertext += table[row_b][col_a]

    return ciphertext


if __name__ == "__main__":
    name = "денисевгеньевич"
    key = "епифанов"

    encrypted = encrypt_playfair(name, key)
    print(f"Зашифрованное сообщение: {encrypted}")


