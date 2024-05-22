alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впр").replace("-", "трэ").replace(" ", "прб").upper())
n = []

p = 10

for i in range(len(shifr)):
    n.append(((alp.index(shifr[i])) % 6 + 1) + (p * (((alp.index(shifr[i])) // 6) + 1)))

print("Открытый текст: ", text)

print("Шифр текст: ", n)

crypt_text_ras = ("")

for i in range(len(shifr)):
    crypt_text_ras = crypt_text_ras + str(alp[(((n[i]//10)-1)*6 + (n[i] % 10)) - 1])

shifr = (crypt_text_ras.lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впр", "?").replace("трэ", "-").replace("прб", " "))
print("Расшифрованный текст: ", shifr)