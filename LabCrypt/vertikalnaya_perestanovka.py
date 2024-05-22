alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впр").replace("-", "трэ").replace(" ", "прб").upper())
n = []
kvadrat = []

keyarr = list(input("Введите ключ: "))
count = 1
ordarr = []
num = 0
flag = 0

shifr_ros = ""
shifr_ras = ""

max_ind = 0 #Преобразование слова в числовой ключ
for i in range(len(keyarr)):
    ordarr.append(ord(keyarr[i]))
    keyarr[i] = str(ord(keyarr[i]))
ordarr.sort()
key = [""] * len(keyarr)
ordarr = [str(x) for x in ordarr]
for i in ordarr:
    ind = keyarr.index(i)
    keyarr[ind] = 0
    key[ind] = str(count)
    count += 1
print(key)
for i in range(len(shifr) // len((key)) + 1):
    kvadrat.append([])
    for j in range(len(key)):
        kvadrat[i].append(shifr[num])
        num += 1
        if num >= len(shifr):
            flag = 1
            break
    if flag == 1:
        break
if len(kvadrat[-1]) < len(kvadrat[-2]):
    raznica = len(kvadrat[-2]) - len(kvadrat[-1])
    for i in range(raznica):
        kvadrat[-1].append("")

for i in range(len(kvadrat)):
    print(kvadrat[i])

for i in range(1, len(key) + 1):
    for j in range(len(kvadrat)):
        shifr_ros += kvadrat[j][key.index(str(i))]

print("Зашифрованное сообщение:", shifr_ros)

for i in range(0, len(kvadrat)):
    shifr_ras += "".join(kvadrat[i])

shifr = (''.join(shifr_ras).lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрс", "?").replace("трэ", "-").replace("прб", " "))
print("Расшифрованный текст: ", shifr)
