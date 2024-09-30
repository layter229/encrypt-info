def to_key(fio):
    vowels = 'АЯУЮИЫОЁЭЕ'
    key = ''
    for char in fio:
        if char.upper() in vowels:
            key += '0'
        else:
            key += '1'
    return key[:10]  # Возвращаем только первые 10 бит


def generate_subkeys(key):
    # Простая схема генерации двух подключей из 10-битного ключа
    # Для примера используем первые 8 бит как первый ключ, последние 2 - второй
    k1 = key[:8]  # Первый ключ (8 бит)
    k2 = key[2:10]  # Второй ключ (8 бит)
    return k1, k2


def sdes_encrypt(block, k1, k2):
    # Заглушка для шифрования (функция шифрования S-DES)
    # Здесь следует реализовать реальный алгоритм S-DES.
    # Для примера просто инвертируем биты.
    return ''.join('1' if bit == '0' else '0' for bit in block)


def to_binary_ascii(text):
    return [format(ord(char), '08b') for char in text]


def binary_to_decimal(binary_str):
    return int(binary_str, 2)


def encrypt_fio(fio):
    fio = fio.replace(" ", "")[:10]
    key = to_key(fio)

    k1, k2 = generate_subkeys(key)

    # берем первые 5 букв
    text_to_encrypt = fio[:5]

    # преобразуем каждую букву в ASCII и переводим в 8-битное представление
    ascii_binaries = to_binary_ascii(text_to_encrypt)

    # шифруем каждый 8-битный блок
    encrypted_blocks = []
    for binary in ascii_binaries:
        encrypted = sdes_encrypt(binary, k1, k2)
        encrypted_blocks.append(encrypted)

    # преобразуем в десятичный формат
    decimal_outputs = [binary_to_decimal(block) for block in encrypted_blocks]

    return decimal_outputs


if __name__ == "__main__":
    fio = "ЕпифановДенисЕвгеньевич"
    result = encrypt_fio(fio)
    print("Зашифрованные десятичные значения:", result)
