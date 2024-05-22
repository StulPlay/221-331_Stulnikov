alp = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ"
text = str(input("Открытый текст: "))
fig = 0

shifr = (text.replace(",", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впрc").replace("-", "трэ").replace(" ", "прб").replace("й","клмн").replace("ъ", "тврд").upper())
n = []
y = 0
t = 0
shifr_new  = ""
shifr_vvod = []
shifr_vvod_ras = []
dob = []
dobf = []

for i in range(0, len(shifr) * 2):
    if len(shifr) <= i + 1:
        break

    if (shifr[i] == shifr[i+1]) and (shifr[i] != "Ф"):
        shifr_new = shifr[:i+1] + "Ф" + shifr[i+1:]
        shifr = shifr_new
        dob.append(i+1)
    if (shifr[i] == shifr[i+1]) and (shifr[i] == "Ф"):
        shifr_new = shifr[:i + 1] + "Ы" + shifr[i + 1:]
        shifr = shifr_new
        dobf.append(i + 1)

if len(shifr) % 2 == 1:
    shifr += "А"
    fig = 1

shifr_slovo = input("Введите ключ: ").upper().replace("й", "и").replace("ъ", "ь")
flag = 0
num = 0
for i in range(len(shifr)):
    n.append(alp.index(shifr[i]) + 1)


key_set = set(shifr_slovo)

if len(key_set) == len(shifr_slovo):
    kvadrat = [[], [], [], [], []]

    for i in range(5):
        for j in range(6):
            if len(shifr_slovo) > i * 6 + j:
                kvadrat[i].append(shifr_slovo[i * 6 + j])
                num += 1
            else:
                flag = 1
                break
        if flag == 1:
            break

    for i in range(len(alp)):
        if alp[i] in shifr_slovo:
            continue
        else:
            kvadrat[num // 6].append(alp[i])
            num += 1

    for i in range(len(kvadrat)):
        print(kvadrat[i])

    for i in range(0, len(shifr) - 1, 2):
        proverka = 0
        for j in range(5):
            if (shifr[i] in kvadrat[j]) and (shifr[i + 1] in kvadrat[j]):
                shifr_vvod.append(kvadrat[j][(1 + kvadrat[j].index(shifr[i])) % 6])
                shifr_vvod.append(kvadrat[j][(1 + kvadrat[j].index(shifr[i + 1])) % 6])
                proverka = 1

        flagvhod = 0
        for j in range(6):
            for k in range(5):
                if shifr[i] == kvadrat[k][j]:
                    flagvhod += 1
                    y = k
                if shifr[i + 1] == kvadrat[k][j]:
                    flagvhod += 1
                    t = k

            if flagvhod == 2:
                shifr_vvod.append(kvadrat[(y + 1) % 5][j])
                shifr_vvod.append(kvadrat[(t + 1) % 5][j])
                proverka = 1
            flagvhod = 0

        if proverka == 0:
            shifr_vvod.append(kvadrat[y][kvadrat[t].index(shifr[i + 1])])
            shifr_vvod.append(kvadrat[t][kvadrat[y].index(shifr[i])])

    print("\n", shifr_vvod)
    shifr_ras = "".join(shifr_vvod)

    for i in range(0, len(shifr_ras) - 1, 2):
        proverka = 0
        for j in range(5):
            if (shifr_ras[i] in kvadrat[j]) and (shifr_ras[i + 1] in kvadrat[j]):
                shifr_vvod_ras.append(kvadrat[j][(kvadrat[j].index(shifr_ras[i]) - 1) % 6])
                shifr_vvod_ras.append(kvadrat[j][(kvadrat[j].index(shifr_ras[i + 1]) - 1) % 6])
                proverka = 1

        flagvhod = 0
        for j in range(6):
            for k in range(5):
                if shifr_ras[i] == kvadrat[k][j]:
                    flagvhod += 1
                    y = k
                if shifr_ras[i + 1] == kvadrat[k][j]:
                    flagvhod += 1
                    t = k

            if flagvhod == 2:
                shifr_vvod_ras.append(kvadrat[(y - 1) % 5][j])
                shifr_vvod_ras.append(kvadrat[(t - 1) % 5][j])
                proverka = 1
            flagvhod = 0

        if proverka == 0:
            shifr_vvod_ras.append(kvadrat[y][kvadrat[t].index(shifr_ras[i + 1])])
            shifr_vvod_ras.append(kvadrat[t][kvadrat[y].index(shifr_ras[i])])

    if fig == 1:
        shifr_vvod_ras.pop(-1)

    for i in reversed(range(len(dob))):
        shifr_vvod_ras.pop(dob[i])

    for i in reversed(range(len(dobf))):
        shifr_vvod_ras.pop(dobf[i])

    shifr = (''.join(shifr_vvod_ras).lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрс", "?").replace("трэ", "-").replace("прб", " "))
    print("Расшифрованный текст: ", shifr)
else:
    print("Ключ не подходит под условие, шифрование не возможно.")

