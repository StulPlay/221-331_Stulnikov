import Modular

k = 0
p = int(input("Введите P: "))
for i in range(2, p // 2 + 1):
    if (p % i == 0):
        k = k + 1
if (p < 32) or (k > 0):
    print("P должно быть больше мощности алфавита и простое.")
    exit()

g = int(input("Введите G: "))
if (g <= 1) or (g >= p):
    print("G дожно быть больше 1 и меньше P")
    exit()

x = int(input("Введите X: "))
if (x <= 1) or (x >= p):
    print("X дожно быть больше 1 и меньше P")
    exit()

k = [7, 11, 13]

alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = input("Открытый текст: ")

text = text.upper()
text = text.replace(".", "ТЧК")
text = text.replace(",", "ЗПТ")

print("ключи:")
print("p =", p)
print("x =", x)
print("g =", g)
y = (g**x) % p
print("y =", y)
print()

res_s = ""
n = []
l = 0

for i in range(len(text)):
    n.append(alp.index(text[i]) + 1)

for i in range(len(text)):
    a = (g**k[l]) % p
    if a < 10:
        res_s = res_s + "0" + str(a)
    else:
        res_s = res_s + str(a)

    b = ((y**k[l]) * n[i]) % p
    if b < 10:
        res_s = res_s + "0" + str(b)
    else:
        res_s = res_s + str(b)
    if l < 2:
        l += 1
    else:
        l = 0

print("Зашифрованный текст: ", res_s)
print()
decoded_text = ""
for i in range(0, len(res_s), 4):
    a = int(res_s[i] + res_s[i + 1])
    b = int(res_s[i + 2] + res_s[i + 3])
    M = Modular.solve_modular_equation(a**x, b, p)
    decoded_text += alp[int(M) - 1]

decoded_text = decoded_text.replace("ТЧК", ".")
decoded_text = decoded_text.replace("ЗПТ", ",")
decoded_text = decoded_text.replace("ПРБ", " ")
print("Расшифрованный текст: ", decoded_text)
