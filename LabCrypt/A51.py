import random
key = [random.choice([0, 1]) for _ in range(64)]
print("Сгенерированный ключ", *key)

gamm = [0] * 114

x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def F(x, y, z):
    return (x & y) or (x & z) or (y & z)

for i in range(64):
    x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0) ^ key[i])
    y.append(y[1] ^ y.pop(0) ^ key[i])
    z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0) ^ key[i])

for i in range(100):
    f = F(x[10], y[11], z[12])
    if f == x[10]:
        x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
    if f == y[11]:
        y.append(y[1] ^ y.pop(0))
    if f == z[12]:
        z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0))
   

for i in range(114):
    gamm[i] = x[0] ^ y[0] ^ z[0]
    f = F(x[10], y[11], z[12])
    if f == x[10]:
        x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
    if f == y[11]:
        y.append(y[1] ^ y.pop(0))
    if f == z[12]:
        z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0))

res_str = []
alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = input("Открытый текст: ")

text = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впрс").replace("-", "трэ").replace(" ", "прб").upper())


period_check = len(text)
period = period_check * 6
gamm = gamm * (period // 114 + 2)
for i in range(len(text)):
  res_str.append(format(alp.index(text[i])+1, 'b').zfill(6)[0])
  res_str.append(format(alp.index(text[i])+1, 'b').zfill(6)[1])
  res_str.append(format(alp.index(text[i])+1, 'b').zfill(6)[2])
  res_str.append(format(alp.index(text[i])+1, 'b').zfill(6)[3])
  res_str.append(format(alp.index(text[i])+1, 'b').zfill(6)[4])
  res_str.append(format(alp.index(text[i])+1, 'b').zfill(6)[5])

res_encrypted = ""
print()
for i in range(period):
    res_encrypted = res_encrypted + str(int(res_str[i]) ^ gamm[i])

print("Зашифрованный текст: ",res_encrypted)

res_decrypted = ""
for i in range(period):
    res_decrypted = res_decrypted + str(int(res_encrypted[i]) ^ gamm[i])

decoded_text = ""
for i in range(0, len(res_str), 6):
    bits = res_decrypted[i:i+6]
    decoded_text += alp[int(bits, 2) - 1]

decoded_text = (''.join(decoded_text).lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрс", "?").replace("трэ", "-").replace("прб", " "))

print("Расшифрованный текст: ", decoded_text)