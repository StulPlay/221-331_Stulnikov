alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впрс").replace("-", "трэ").replace(" ", "прб").upper())
keyvod = input("Введите ключ: ")
key = str(keyvod[0] + shifr).upper()
n = []

print("Выбран ключ: " + keyvod[0])

for i in range(len(shifr)):
    n.append(alp[(alp.find(shifr[i]) + (alp.find(key[i % len(key)]))) % 32])

print("Открытый текст: ", text)

print("Шифр текст: ", ''.join(n))
ras = []
for i in range(len(shifr)):
    ras.append(alp[(alp.find(n[i]) - (alp.find(key[i % len(key)]))) % 32])


shifr = (''.join(ras).lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрс", "?").replace("трэ", "-").replace("прб", " "))
print("Расшифрованный текст: ", shifr)
