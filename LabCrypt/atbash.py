alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впр").replace("-", "трэ").replace(" ", "прб").upper())
n = []

alp_rev = alp[::-1]

for i in range(len(shifr)):
    n.append(alp.index(shifr[i]) + 1)

crypt_text = ("")
crypt_text_ras = ("")

for i in range(len(shifr)):
    crypt_text = crypt_text + str(alp_rev[n[i] - 1])

print("Открытый текст: ", text)

print("Шифр текст: ", crypt_text)

for i in range(len(shifr)):
    crypt_text_ras = crypt_text_ras + str(alp[n[i] - 1])


shifr = (crypt_text_ras.lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впр", "?").replace("трэ", "-").replace("прб", " "))
print("Расшифрованный текст: ", shifr)