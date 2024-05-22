import Modular

k = 0
p = int(input("Введите P: "))
for i in range(2, p // 2+1):
    if (p % i == 0):
        k = k+1
if (p < 32) or (k > 0):
    print("P не подходит под условие.")
    exit()

g = int(input("Введите G: "))
if (g <= 1) or (g >= p):
    print("G не подходит под условие.")
    exit()

x = int(input("Введите X: "))
if (x <= 1) or (x >= p):
    print("X не подходит под условие.")
    exit()

k = 7

alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
shifr = str(input("Открытый текст: "))
text = (shifr.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впр").replace("-", "трэ").replace(" ", "прб").replace("ё", "е").upper())


print("Открытые ключи:")
print("p =", p)
print("x =", x)
print("g =", g)
y = (g**x) % p
print("Секретный ключ:")
print("y =", y)
print()


mas_i = []
for i in range(len(text)):
    mas_i.append(alp.index(text[i])+1)

print("Открытый текст:", shifr)
print()

h = []
ph = 32
for i in range(len(text)):
    if i == 0:
        h.append(((0 + mas_i[i]) ** 2) % ph)
    else:
        h.append(((h[i-1] + mas_i[i]) ** 2) % ph)

p = 41
a = (g ** k) % p

af = k
bf = -(x * a - h[len(text) - 1])
mf = p - 1
b = Modular.solve_modular_equation(af, bf, mf)

print(f"Цифровая подпись: S = ({a}, {b})")
print()

if b is not None:
    a1 = ((y ** a) * (a ** b)) % p
    a2 = (g ** h[len(text) - 1]) % p
    print("Проверка:", a1, "=", a2)