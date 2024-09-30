# alf = ['а','б','в','г','д','е','ё','ж','з','и','й',
#        'к','л','м','н','о','п','р','с','т','у','ф',
#        'х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
decrypted = []
crypt = []
alf = { 0: 'А', 1: 'Б', 2: 'В', 3: 'Г', 4: 'Д', 5: 'Е', 6: 'Ё', 7: 'Ж', 8: 'З', 9: 'И', 10: 'Й', 11: 'К', 12: 'Л', 13: 'М', 14: 'Н', 15: 'О', 16: 'П', 17: 'Р', 18: 'С',  19: 'Т',  20: 'У',  21: 'Ф',  22: 'Х',  23: 'Ц',  24: 'Ч',  25: 'Ш', 26: 'Щ',  27: 'Ъ', 28: 'Ы', 29: 'Ь',  30: 'Э',  31: 'Ю',  32: 'Я'}

result1 = []
result2 = []


def cezar_encrypt(fio):
    for i in range(len(fio)):
        for x in range(len(alf)):
            if alf[x] == fio[i]:
                decrypted.append(x)


    for k in range(len(decrypted)):
        crypt.append(decrypted[k] + 3)



    # for k in range(len(decrypted)):
    #     print(alf.get())

    for c in range(len(decrypted)):
        result1.append(alf.get(decrypted[c]))
        print(alf.get(decrypted[c]) + '---' + str(decrypted[c]))

    for c in range(len(crypt)):
        result2.append(alf.get(crypt[c]))
        print(alf.get(crypt[c]) + '---' + str(crypt[c]))

    print(result1)
    print(result2)

if __name__ == "__main__":
    fio = "ЕПИФАНОВ ДЕНИС ЕВГЕНЬЕВИЧ"
    encrypted = cezar_encrypt(fio)
