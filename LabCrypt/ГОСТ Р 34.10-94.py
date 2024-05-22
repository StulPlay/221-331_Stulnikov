p = int(input("Введите p (простое число большее 1): "))
k = 0

#Ввод ключей и проверка их на условия
for i in range(2, p // 2+1):
    if (p % i == 0):
        k = k+1
if (k > 0) and p > 1:
   print("p должно быть простое и большее 1")
   exit()
q = int(input(f"Введите q (простой сомножитель числа {p-1}): "))

d = 3
x = int(input("Введите x (меньшее q и большее 1): "))
if x >= q and x > 1:
   print("x должно быть меньше q и больше 1")
   exit()
a = (d**((p-1)//q)) % p

y = (a**x) % p
k = int(input("Введите k (меньшее q): "))
if k >= q:
    print("k должно быть меньше q")
    exit()

#Вывод ключей
print()
print("Секретный ключ: ")
print("x =", x)
print()
print("Открытые ключи: ")
print("p =", p)
print("q =", q)
print("d =", d)
print("a =", a)
print("y =", y)
print("k =", k)
print()

#Определение алфавита
alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

#Ввод фразы для шифрования
shifr = "КТОБОИТСЯКАЖДОГОКУСТАЗПТНИКОГДАНЕДОЛЖЕНХОДИТЬНАЛОВЛЮПТИЦТЧК"
text = (shifr.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впр").replace("-", "трэ").replace(" ", "прб").upper())

#Шифрование
mas_i = []
for i in range(len(text)):
  mas_i.append(alp.index(text[i])+1)

h = []
ph = 32
for i in range(len(text)):
  if i == 0:
    h.append(((0 + mas_i[i]) ** 2) % ph)
  else:
    h.append(((h[i-1] + mas_i[i]) ** 2) % ph)

r = (a ** k % p) % q
s = (x * r + k * h[len(text) - 1]) % q
print(f"Цифровая подпись: r = {r}, s = {s}")

#Проверка цифровой подписи
print()
v = ((h[len(text) - 1]) ** (q-2)) % q
print("v =", v)
z1 = (s * v) % q
z2 = ((q - r) * v) % q
u = ((a**z1 * y ** z2) % p) % q
print("z1 =", z1)
print("z2 =", z2)
print("u =", u)
print()
print("Проверка: u =",u,", r =", r)
if u == r:
    print("Цифровая подпись верна")
else:
    print("Цифровая подпись не верна")
