alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впр").replace("-", "трэ").replace(" ", "прб").upper())
n = []


for i in range(len(shifr)):
    n.append(alp.index(shifr[i]) + 1)

crypt = []
crypt_ras = []
crypt_text = ("")
crypt_text_ras = ("")

print("Введите ключ: ")
key = int(input())

while key >= len(alp) or key < 1:
    print("Ключ не удовлетворяет условиям.")
    print("Введите новый ключ: ")
    key = int(input())

for i in range(len(shifr)):
    if n[i] + key > 32:
        crypt.append(n[i] + key - 32)
    else:
        crypt.append(n[i] + key)

for i in range(len(shifr)):
    crypt_text = crypt_text + str(alp[crypt[i] - 1])

print("Открытый текст: ", text)

print("Шифр текст: ", crypt_text)

for i in range(len(shifr)):
    if crypt[i] - key < 0:
        crypt_ras.append(crypt[i] - key + 32)
    else:
        crypt_ras.append(crypt[i] - key)

for i in range(len(shifr)):
    crypt_text_ras = crypt_text_ras + str(alp[crypt_ras[i] - 1])


shifr = (crypt_text_ras.lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впр", "?").replace("трэ", "-").replace("прб", " "))
print("Расшифрованный текст: ", shifr)