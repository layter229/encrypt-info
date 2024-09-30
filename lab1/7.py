def vertical_permutation_encrypt(text, key):
    text = text.replace(" ", "").upper()
    num_columns = len(key)
    num_rows = (len(text) + num_columns - 1) // num_columns
    table = ['' for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            if index < len(text):
                table[i] += text[index]

    key_indices = sorted(range(len(key)), key=lambda x: key[x])
    encrypted_text = ''
    for index in key_indices:
        for row in table:
            if index < len(row):
                encrypted_text += row[index]

    return encrypted_text


if __name__ == "__main__":
    text = "ЕпифановДенисЕвгеньевич"
    key = "5341726"
    encrypted_text = vertical_permutation_encrypt(text, key)
    print(f'Зашифрованный текст: {encrypted_text}')
