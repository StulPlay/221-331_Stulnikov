import math
import Modular

def calculate_plus(x1, y1, x2, y2, p):
    # Расчет U31, U32, U3
    U1 = (y2 - y1) % p
    U2 = (x2 - x1) % p
    U = (U1 * (U2 ** (p-2))) % p

    # Расчет new_x и new_y
    new_x = (U ** 2 - x2 - x1) % p
    new_y = (-y2 - U * (new_x - x2)) % p

    return new_x, new_y


def calculate_mult(x, y, p):
    # Расчет U11, U12, U1
    U1 = (3 * (x ** 2) + a) % p
    U2 = (2 * y) % p
    U = (U1 * (U2 ** (p-2) % p)) % p

    # Расчет new_x и new_y
    new_x = (U ** 2 - 2 * x) % p
    new_y = (-(y + U * (new_x - x))) % p

    return new_x, new_y

def perform_actions(t, x0, y0, p):
    # print(t, x0, y0, p)
    actions = split_number(t)
    # print(f"Для получения числа {Cb} из единицы нужно выполнить следующие действия:")
    # print(actions)
    result = [x0, y0]  # Начинаем с 1, так как операции начинаются с единицы
    for action in actions:
        if action == '+1':
            result = calculate_plus(x0, y0, result[0], result[1], p)
            # print(result)
        elif action == '*2':
            result = calculate_mult(result[0], result[1], p)
            # print(result)
    return result

def split_number(n):
    actions = []
    while n > 1:
        if n % 2 == 0:
            actions.append('*2')
            n //= 2
        else:
            actions.append('+1')
            n -= 1
    actions.reverse()
    return actions

alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = input("Введите текст: ")
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впрс").replace("-", "трэ").replace(" ", "прб").upper())
n = []
print("Открытый текст:", text)
print()
crypt = ""
P = (0, 0)
Q = (0, 1)


for i in range(len(shifr)):
    n.append(alp.index(shifr[i]) + 1)

x0 = 10
y0 = 5
G = (x0, y0)

a = 2
b = 6
m = 10
XU = 5

p = 11
q = 7

# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# Cb = int(input("Введите Cb: "))
# k = int(input("Введите k: "))
# p = int(input("Введите простое p: "))
# print()

YU = perform_actions(XU, G[0], G[1], p)
print("Точка кривой YU:", YU)

h = []
for i in range(len(text)):
  if i == 0:
    h.append(((0 + n[i]) ** 2) % p)
  else:
    h.append(((h[i-1] + n[i]) ** 2) % p)


print("Хеш:", h[len(text) - 1])

k = 4

P = perform_actions(k, G[0], G[1], p)
print("Точка кривой P:", P)

r = P[0] % q
print("r =", r)

s = (k * h[len(text) - 1] + r * XU) % q
print("s =", s)

print(f"Цифровая подпись {r, s}")

u1 = (s * (h[len(text) - 1]) ** (q-2)) % q
print("u1 =", u1)

u2 = ((-r) * (h[len(text) - 1]) ** (q-2)) % q
print("u2 =", u2)

P1 = perform_actions(u1, G[0], G[1], p)
P2 = perform_actions(u2, YU[0], YU[1], p)

if (P1[0] == P2[0]) and (P1[1] == P2[1]):
    Q = calculate_mult(P1[0], P1[1], p)
    print("Точка кривой P:", Q)
else:
    Q = calculate_plus(P1[0], P1[1], P2[0], P2[1], p)
    print("Точка кривой P:", Q)

r1 = Q[0] % q
if r1 == r:
    print("Подпись верна: r1 = r;", r1, "=", r)
else:
    print("Подпись не верна: r1 <> r", r1, "<>", r)
