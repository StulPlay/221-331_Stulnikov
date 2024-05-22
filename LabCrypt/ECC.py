from sympy.ntheory import factorint
from random import randint

def choose_base_point(a, b, p):
    order_n = p
    prime_factors = factorint(order_n)
    prime_order_q = max(prime_factors)
    cofactor = order_n // prime_order_q

    while True:
        x = randint(0, p)
        y_sq = (x**3 + a * x + b) % p
        y = pow(y_sq, (p + 1) // 4, p)
        base_point_x, base_point_y = calculate_mult(x, y, p)

        if (base_point_x, base_point_y) != (0, 0):
            return base_point_x, base_point_y

def check_inf(x, y, p, n):
    if n == 0:
        return [0, 0]
    elif n == 1:
        return n

    point_res = [x, y]
    point_start = [x, y]
    point_res = calculate_mult(point_res[0], point_res[1], p)

    for infinity in range(2, n):
        point_res = calculate_plus(point_start[0], point_start[1], point_res[0], point_res[1],  p)
        #print(point_res, infinity)
        if point_res == ["inf", "inf"]:
            infinity += 1
            if infinity == n:
                return ["inf", "inf"]
            return infinity
    return n

def calculate_plus(x1, y1, x2, y2, p):
    # Расчет U31, U32, U3
    U1 = (y2 - y1) % p
    U2 = (x2 - x1) % p
    U = (U1 * (U2 ** (p-2))) % p

    # Расчет new_x и new_y
    new_x = (U ** 2 - x2 - x1) % p
    new_y = (-y2 - U * (new_x - x2)) % p

    if U2 == 0:
        return ["inf", "inf"]

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
text = str(input("Открытый текст: "))
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впрс").replace("-", "трэ").replace(" ", "прб").upper())
n = []
print("Открытый текст:", text)
print()
crypt = ""
P = (0, 0)
Q = (0, 1)


for i in range(len(shifr)):
    n.append(alp.index(shifr[i]) + 1)

# a = 2
# b = 6
# Cb = 9
# k = 5
# p = 41


x0 = 10
y0 = 5
G = (x0, y0)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
Cb = int(input("Введите Cb: "))
k = int(input("Введите k: "))
p = int(input("Введите простое p: "))
# print()

while P != Q:
    base_point = choose_base_point(a, b, p)
    # print((check_inf(base_point[0], base_point[1], p, 1000)))
    if (check_inf(base_point[0], base_point[1], p, 1000)) % Cb == 0:
        # print("Точка улетела в 0:", (check_inf(base_point[0], base_point[1], p, 1000)))
        while (check_inf(base_point[0], base_point[1], p, 1000)) % Cb == 0:
            base_point = choose_base_point(a, b, p)
            # print("Точка улетела в 0:", check_inf(base_point[0], base_point[1], p, 1000))
    # else:
    #     print("Точка не улетела в 0:")

    # print("Базовая точка:", base_point)

    Db = perform_actions(Cb, G[0], G[1], p)
    # print("Открытый ключ Db:", Db)

    R = perform_actions(k, G[0], G[1], p)
    # print("Точка кривой R:", R)

    P = perform_actions(k, Db[0], Db[1], p)
    # print("Точка кривой P:", P)

    Q = perform_actions(Cb, R[0], R[1], p)


print("Базовая точка:", base_point)
print("Открытый ключ Db:", Db)
print("Точка кривой R:", R)
print("Точка кривой P:", P)
# print("Точка кривой Q:", Q)

E = []
M = []
print()
print('Зашифрованный текст: ', end="")
for i in range(len(shifr)):
    e = (n[i] * P[0]) % p
    E.append(e)
    print(f'{R,e}', end=' ')
print()

for i in range(len(shifr)):
    m = (E[i] * Q[0] ** (p-2)) % p
    M.append(m)
# print(n)
# print(M)

for i in range(len(shifr)):
    crypt = crypt + str(alp[M[i] - 1])


shifr = (''.join(crypt).lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрс", "?").replace("трэ", "-").replace("прб", " "))
print("Расшифрованный текст:", shifr)