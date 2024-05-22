import math

alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впр").replace("-", "трэ").replace(" ", "прб").upper())
n = []
crypt = []
shifr_text = []
shifr_text_ras = []

for i in range(len(shifr)):
    n.append(alp.index(shifr[i]) + 1)

m = len(alp)
T = []
T0 = int(input("Введите T0: "))
a = int(input("Введите a: "))
c = int(input("Введите c: "))
if (T0 > 0) and (T0 < m):
    if (a % 2 == 1) and (a > 1) and (a < m):
        if (math.gcd(c, m) == 1) and (c % 2 == 1):
            T.append(T0)
            for i in range(len(text)):
                T.append(a * T[i] + c % m)
                crypt.append(T[i+1])

            for i in range(len(text)):
                shifr_text.append(alp[(crypt[i] + n[i]) % 32 - 1])

            print("Зашифрованный текст: ", "".join(shifr_text))

            for i in range(len(text)):
                shifr_text_ras.append(alp[(alp.index(shifr_text[i]) - crypt[i] + 1) % 32 - 1])
            shifr = (''.join(shifr_text_ras).lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрс","?").replace("трэ", "-").replace("прб", " "))
            print("Расшифрованный текст: ", shifr)
        else:
            print("C не подходит под условие, шифрование не возможно.")
    else:
        print("A не подходит под условие, шифрование не возможно.")
else:
    print("T0 не подходит под условие, шифрование невозможно.")