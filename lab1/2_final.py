import re

def create_playfair_table(key):
    alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюя"
    key = re.sub(r'[^а-я]', '',
                 key.lower().replace("ё", "е").replace("й", "и"))
    table = []
    used_letters = set()

    for char in key:
        if char not in used_letters and char in alphabet:
            table.append(char)
            used_letters.add(char)

    for char in alphabet:
        if char not in used_letters:
            table.append(char)

    table = [table[i:i + 6] for i in range(0, len(table), 6)]
    return table


def find_position(table, char):
    for row in range(len(table)):
        if char in table[row]:
            return row, table[row].index(char)
    return None


def encrypt_playfair(plaintext, key):
    table = create_playfair_table(key)
    plaintext = re.sub(r'[^а-я]', '', plaintext.lower().replace("ё", "е").replace("й", "и"))

    digraphs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
            if a == b:
                b = 'я' if a != 'я' else 'а'  # разделитель
            else:
                i += 1
        else:
            b = 'я'  # без пары
        digraphs.append((a, b))
        i += 1

    ciphertext = ''


    for a, b in digraphs:
        row_a, col_a = find_position(table, a)
        row_b, col_b = find_position(table, b)

        if row_a == row_b:
            # если символы в одной строке, сдвигаем вправо
            ciphertext += table[row_a][(col_a + 1) % 6]
            ciphertext += table[row_b][(col_b + 1) % 6]
        elif col_a == col_b:
            # если символы в одном столбце, сдвигаем вниз
            ciphertext += table[(row_a + 1) % 5][col_a]
            ciphertext += table[(row_b + 1) % 5][col_b]
        else:
            # если символы находятся в разных строках и столбцах, меняем столбцы
            ciphertext += table[row_a][col_b]
            ciphertext += table[row_b][col_a]

    return ciphertext


if __name__ == "__main__":
    name = "денисевгеньевич"
    key = "епифанов"

    encrypted = encrypt_playfair(name, key)
    print(f"Зашифрованное сообщение: {encrypted}")


