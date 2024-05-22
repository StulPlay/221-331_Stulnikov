import math
import Modular
alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
mas_i = []

shifr = str(input("Открытый текст: "))
text = (shifr.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впр").replace("-", "трэ").replace(" ", "прб").replace("ё", "е").upper())


for i in range(len(text)):
    mas_i.append(alp.index(text[i])+1)

res_s = ""
res_ras = ""
shifr_text_ras = []
P = int(input("Введите P: "))
Q = int(input("Введите Q: "))

k = 0
for i in range(2, P // 2+1):
    if (P % i == 0):
        k = k+1

if (k <= 0):
    k = 0
    for i in range(2, Q // 2 + 1):
        if (Q % i == 0):
            k = k + 1
    if (k <= 0):
        N = P * Q
        F_N = (P - 1) * (Q - 1)
        if N >= 33:
            print("Введите E, взаимно простое с", F_N, ": ")
            E = int(input())
            if math.gcd(N, E) == 1:
                print("E = ", E, " N = ", N)
                D = Modular.solve_modular_equation(E, 1, F_N)
                print("D = ", D)
                h = []

                for i in range(len(text)):
                    if i == 0:
                        h.append(((0 + mas_i[i]) ** 2) % 32)
                    else:
                        h.append(((h[i - 1] + mas_i[i]) ** 2) % 32)

                S = ((h[len(text) - 1] ** D) % N)

                print("Открытый текст:", shifr)
                print("m =", h[len(text) - 1])
                print("ЭЦП:", S)

                m_ch = ((S ** E) % N)

                print("m' = ", m_ch)

                if h[len(text) - 1] == m_ch:
                    print("Проверка: m =", h[len(text) - 1], "m' =", m_ch)
                    print("Цифровая подпись верна.")
                else:
                    print("Проверка: m =", h[len(text) - 1], "m' =", m_ch)
                    print("Цифровая подпись не верна.")



            else:
                print("Числа P и Q не подходят под условие.")
        else:
          print("Числа P и Q не подходят под условие.")
    else:
        print("Число P не подходит под условие.")
else:
    print("Число Q не подходит под условие.")

