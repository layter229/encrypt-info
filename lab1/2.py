import numpy as np

alf = {0: 'А', 1: 'Б', 2: 'В', 3: 'Г', 4: 'Д', 5: 'Е', 6: 'Ж', 7: 'З', 8: 'И', 9: 'К', 10: 'Л',
       11: 'М', 12: 'Н', 13: 'О', 14: 'П', 15: 'Р', 16: 'С', 17: 'Т', 18: 'У', 19: 'Ф', 20: 'Х', 21: 'Ц', 22: 'Ч',
       23: 'Ш', 24: 'Щ', 25: 'Ъ', 26: 'Ы', 27: 'Ь', 28: 'Э', 29: 'Ю', 30: 'Я'}


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

encrypt_key = input("Введите ключ зашифровки: ")
text = input("Введите текст зашифровки: ")

mas = []
for i in range(0, len(text), 2):
    element = text[i:i + 2]
    if len(element) == 1:
        mas.append(element + 'я')
    else:
        mas.append(element)

print(mas)


