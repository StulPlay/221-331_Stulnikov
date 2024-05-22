alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
key = input("Введите ключ: ")
key = key.upper()
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впрc").replace("-", "трэ").replace(" ", "прб").upper())
n = []

for i in range(len(shifr)):
    n.append(alp[(alp.find(shifr[i]) + (alp.find(key[i % len(key)]))) % 32])

print("Открытый текст: ", text)

print("Шифр текст: ", ''.join(n))
ras = []
for i in range(len(shifr)):
    ras.append(alp[(alp.find(n[i]) - (alp.find(key[i % len(key)]))) % 32])


shifr = (''.join(ras).lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрc", "?").replace("трэ", "-").replace("прб", " "))
print("Расшифрованный текст: ", shifr)
