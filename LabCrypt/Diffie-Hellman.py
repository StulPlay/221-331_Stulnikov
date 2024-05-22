#Ввод чисел a и n
a = int(input("Введите A большее 1: "))
if a <= 1:
    print("A должно быть больше 1")
    exit()

n = int(input("Введите N большее A: "))
if n <= a:
    print("N должно быть больше A")
    exit()

#Определение секретных ключей пользователей КА и КВ.
ka = int(input(f"Введите K(a) не меньше 2 и не больше {n-1}: "))
if (ka < 2) or (ka > n-1):
    print(f"K(a) должно быть не меньше 2 и не больше {n-1}")
    exit()

kb = int(input(f"Введите K(b) не меньше 2 и не больше {n-1}: "))
if (kb < 2) or (kb > n-1):
    print(f"K(b) должно быть не меньше 2 и не больше {n-1}")
    exit()

#Вычисление открытых ключей пользователей
ya = (a ** ka) % n
yb = (a ** kb) % n

#Проверка ключей
if (ya == 1) or (yb == 1):
    print("\nЕдиничный ключ. Введите другие параметры.")
    exit()

#Обмен ключами YA и YB по открытому каналу связи.
print("Обмен ключами: ")
print(f"Ya = {ya}")
print(f"Yb = {yb}")

#Независимое определение общего секретного ключа К
ka1 = (ya ** ka) % n
kb1 = (yb ** kb) % n

#Проверка ключей
if (ka1 == 1) or (kb1 == 1):
    print("\nЕдиничный ключ. Введите другие параметры.")
    exit()

if ka1 == kb1:
    print("Ka = Kb = K")
    print(f"{ka1} = {kb1} = {ka1}")
else:
    print("Ka не равно Kb, введите другие параметры")
