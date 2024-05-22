import numpy as np

def inverse_matrix(matrix):
    try:
        # Преобразуем входную матрицу в массив numpy
        matrix_np = np.array(matrix)

        # Вычисляем обратную матрицу
        inverse_np = np.linalg.inv(matrix_np)

        return inverse_np.tolist()  # Преобразуем результат обратно в обычный список
    except np.linalg.LinAlgError:
        return None

def matrix_multiplication(A, B):
    result = []

    # Перемножаем матрицы
    for i in range(len(A)):
        # Для каждой строки матрицы A
        row_result = 0
        for j in range(len(B)):
            # Для каждого столбца матрицы B
            row_result += A[i][j] * B[j]
        result.append(row_result)

    return result


alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = str(input("Открытый текст: "))
shifr = (text.replace("),", "зпт").replace(".", "тчк").replace("!", "вскл").replace("?", "впрс").replace("-", "трэ").replace(" ", "прб").replace("ё", "е").upper())
n = []
result = []
ras_result = []
crypt_text_ras = ("")

for i in range(len(shifr)):
    n.append(alp.index(shifr[i]) + 1)

print("Введите размерность матрицы:")
p = int(input())

print("Введите элементы матрицы A:")
A = []

for i in range(p):
    row = list(map(int, input().split()))
    A.append(row)

matrix_size = p
n_extended = n + [0] * (matrix_size - len(n) % matrix_size)  # Дополнение нулями до кратности размеру матрицы

matrices = [n_extended[i:i+matrix_size] for i in range(0, len(n_extended), matrix_size)]

for i in range(len(matrices)):
    result.append(matrix_multiplication(A, matrices[i]))

all_result = [str(item) for sublist in result for item in sublist]
result_string = ' '.join(all_result)


inverse_A = (inverse_matrix(A))
if inverse_A != None:
    for i in range(len(matrices)):
        ras_result.append(matrix_multiplication(inverse_A, result[i]))

    all_ras_result = [str(round(float(item))) for sublist in ras_result for item in sublist]
    ras_result_string = ' '.join(all_ras_result)

    print("Зашифрованный текст: ", result_string)

    for i in range(len(shifr)):
        crypt_text_ras = crypt_text_ras + str(alp[int(all_ras_result[i]) - 1])

    shifr = (crypt_text_ras.lower().replace("зпт", ",").replace("тчк", ".").replace("вскл", "!").replace("впрс", "?").replace("трэ", "-").replace("прб", " "))
    print("Расшифрованный текст: ", shifr)
else:
    print("Матрица вырожденная, шифрование невозможно.")
