import math
import Modular
alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
text = text.upper()
mas_i = []
print("Цифровизировать предложение")
for i in range(len(text)):
    print(alp.index(text[i]) + 1, end=" ")
    mas_i.append(alp.index(text[i])+1)

print()
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
        if N >= 33:
            E = 17
            if math.gcd(N, E) == 1:
                print("E = ", E, " N = ", N)
                for i in range(len(text)):
                    num = (mas_i[i] ** E) % N
                    if num < 10:
                      res_s = res_s + " " + str(num)
                    else:
                      res_s = res_s + " " + str(num)
                print("Зашифрованный текст: ", res_s)

                mas_ras = []
                mas_ras = res_s.split()
                F_N = (P-1) * (Q-1)
                D = Modular.solve_modular_equation(E, 1, F_N)
                print("D = ", D)
                for i in range(len(text)):
                    num = (int(mas_ras[i]) ** D) % N
                    if num < 10:
                        res_ras = res_ras + " 0" + str(num)
                    else:
                        res_ras = res_ras + " " + str(num)

                mas_res_ras = []
                mas_res_ras = res_ras.split()

                for i in range(len(mas_res_ras)):
                    shifr_text_ras.append(alp[int(mas_res_ras[i]) - 1])

                shifr = (''.join(shifr_text_ras).lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрc","?").replace("трэ", "-").replace("прб", " "))
                print("Расшифрованный текст: ", shifr)
            else:
                print("Числа P и Q не подходят подходит под второе условие.")
        else:
          print("Числа P и Q не подходят под первое условие.")
    else:
        print("Число P не подходит под условие.")
else:
    print("Число Q не подходит под условие.")

