#найти сумму элементов матрицы, лежащей выше главно
# й диагонали
matrix = [[1, 4, 6],
          [6, 3, 0],
          [2, 9, 4]]
sum = 0
for i in range(0, len(matrix)):
    for j in range(i + 1, len(matrix[i])):
        sum += matrix[i][j]
print(sum)

#Вычислить кол-во положительных элементов квадратной иатрицы
# рассположенных по ее перемитру и на диагоналях
# главная диагональ i == j
# побочная диагональ i + j + 1 == N
#
# первая строка   0,i
# последняя строка    N-1, i
#
# первый столбец  i, 0
# последний столбец   i, N-1

matrix = [[1, -4, 6, 5],
          [-6, 3, 0, -8],
          [2, 9, -4, 2],
          [-3, 6, -1, 9]]
k = 0 #счетчик положительных чисел
N = len(matrix)
for i in range(0, N):
    if matrix [i] [i] > 0:
        k += 1
    if matrix[i][N - i - 1] > 0:
        k += 1
    if 0 < i < N - 1:
        if matrix[0][i] > 0:
            k += 1
        if matrix[N - 1][i] > 0:
            k += 1
        if matrix[i][0] > 0:
            k += 1
        if matrix[i][N - 1] > 0:
            k +=1
if N % 2 != 0 and matrix[N//2][N//2] > 0:
    k -= 1
print(k)
# Поменять местами элементы главной и побочной диагонали
# квадратной матрицы

matrix = [[1, -4, 6, 5],
          [-6, 3, 0, -8],
          [2, 9, -4, 2],
          [-3, 6, -1, 9]]
N = len(matrix)
for i in range(0, N):
    matrix[i][i], matrix[i][N - i - 1] = matrix[i][N - i - 1], matrix[i][i]
print(matrix)


# Усовершенствуйте алгоритм поиска максимального элемента матрицы таким образом,
# чтобы он находил также ее минимальный элемент и его индексы.
# Поменяйте местами максимальный и минимальный элементы

matrix = [[1, 2, 3],
          [4, 5, 2],
          [8, 0, 3]]
max_elem = matrix[0][0]
min_elem = matrix[0][0]
i_max = j_max = 0
i_min = j_min = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
            i_max = i
            j_max = j
        if matrix[i][j] < min_elem:
            min_elem = matrix[i][j]
            i_min = i
            j_min = j
print('max element: ', max_elem, 'string: ',  i_max, 'column: ', j_max)
print('min element: ', min_elem, 'string: ', i_min, 'column: ',  j_min)
matrix[i_max][j_max], matrix[i_min][j_min] = matrix[i_min][j_min], matrix[i_max][j_max]
print(matrix)

#Дана квадратная матрица. Проверьте, является ли она единичной.
matrix = [[1, 0, 0],
          [0, 1, 0],
          [1, 0, 1]]
flag_exit = False
result = 1
for i in range(len(matrix)):
    for j in range(len(matrix)):
        elem = matrix[i][j]
        if (i == j and elem != 1) or (i != j and elem != 0):
            flag_exit = True
            result = 0
            break
    if flag_exit:
        break
print('Matrix' + [' no', ''][result], 'single')

#Преобразуйте исходную матрицу A(n,m) так,
# чтобы первый элемент в каждой ее строке был
# заменен на среднее арифметическое элементов этой строки.
matrix = [[1, 2, 3],
          [4, 5, 2],
          [8, 0, 3]]
# Преобразование матрицы
for row in matrix:
    # Находим сумму элементов в строке
    sum_elem = 0
    for elem in row:
        sum_elem += elem
        # Находим среднее арифметическое элементов строки и округляем его до двух знаков после запятой
        avg_elem_in_string = round(sum_elem / len(row), 2)
    # Заменяем первый элемент в строке на среднее арифметическое
        row[0] = avg_elem_in_string

# Вывод результата
for row in matrix:
    print(row)

#Дана квадратная матрица. Проверьте, является ли она верхнетреугольной.
matrix = [[1, 6, 5],
          [0, 1, 7],
          [5, 0, 1]]
uppercorner = True
for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        elem = matrix[i][j]
        if i > j and matrix[i][j] != 0:
            uppercorner = False
            break
if uppercorner:
    print("Matrix is uppercorner")
else:
    print("Мatrix in not uppercorner")

#Дана квадратная матрица. Проверьте, является ли она симметричной.
matrix = [[1, 3, 0],
          [3, 2, 6],
          [0, 6, 5]]
transposed_matrix = []
for j in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[j])
    transposed_matrix.append(transposed_row)
if transposed_matrix == matrix:
    print('Matrix is symmetrical')
else:
    print('Matrix  in not symmetrical')






