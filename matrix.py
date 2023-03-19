def sum_matrices(a, b):
    '''
    Find sum of 2 matrices
    matrices of equal size :param a:
    matrices of equal size :param b:
    matrix :return:
    '''
    #Получаем размер матриц
    rows = len(a)
    cols = len(a[0])
    rows2 = len(b)
    cols2 = len(b[0])

    #Проверка матриц на кол-во элементов
    if rows != rows2 or cols != cols2:
        raise ValueError('Матрицы разного размера')

    # Создаем новую матрицу, в которую будем записывать сумму двух матриц
    result = [[0 for j in range(cols)] for i in range(rows)]

    # Проходим по каждому элементу матрицы и складываем их
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result

#Умножение
def prod_matrix_scalar(a, b):
    # Получаем размеры матриц
    rows1, cols1 = len(a), len(a[0])
    rows2, cols2 = len(b), len(b[0])

    # Проверяем возможность умножения матриц
    if cols1 != rows2:
        raise ValueError("Умножение матриц невозможно")

    # Создаем новую матрицу, в которую будем записывать произведение двух матриц
    result = [[0 for j in range(cols2)] for i in range(rows1)]

    # Проходим по каждому элементу новой матрицы и вычисляем его
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += a[i][k] * b[k][j]

    return result

#Транспонированая матрица
def transposed_matrix(a):
    # Получаем размеры матрицы
    rows = len(a)
    cols = len(a[0])
    if not all(len(row) == len(a[0]) for row in a):
        raise ValueError("Неравное колисчество строк и столбцов")

    # Создаем новую матрицу, в которую будем записывать транспонированную матрицу
    result = [[0 for j in range(rows)] for i in range(cols)]

    # Проходим по каждому элементу матрицы и записываем его в соответствующую позицию в новой матрице
    for i in range(rows):
        for j in range(cols):
            result[j][i] = a[i][j]

    return result

#Определитель
def determinant(a):
    if len(a) == 1:
        return a[0][0]
    res = 0
    for j in range(0, len(a)):
        #Находим определитель
        res += (-1) ** j * a[0][j] * minor(a, 0, j)
    return res

#Возвращает определитель матрицы в которой вычеркнуты строка row_del и столбец col_del
def minor(a, row_del, col_del):
    res = []
    for i in range(len(a)):
        if i != row_del:
            row = []
            for j in range(len(a)):
                if j != col_del:
                    row += [a[i][j]]
            res += [row]
    return determinant(res)


#Обратная матрица
def reversed_matrix(A):
    # Получаем размер матрицы
    n = len(A)

    # Создаем единичную матрицу той же размерности, что и исходная матрица
    a1 = [[0 if i != j else 1 for j in range(n)] for i in range(n)]

    # Копируем исходную матрицу, чтобы избежать изменения исходной матрицы
    a_copy = [row[:] for row in A]

    # Проходим по каждой строке матрицы
    for i in range(n):
        # Проверяем, что главный элемент в данной строке не нулевой
        if a_copy[i][i] == 0:
            raise ValueError("Матрица вырожденная, обратной матрицы не существует")

        # Делим всю строку на главный элемент
        delitel = a_copy[i][i]
        for j in range(n):
            a_copy[i][j] /= delitel
            a1[i][j] /= delitel

        # Обнуляем все элементы в столбце, кроме главного
        for k in range(n):
            if k == i:
                continue

            factor = a_copy[k][i]
            for j in range(n):
                a_copy[k][j] -= factor * a_copy[i][j]
                a1[k][j] -= factor * a1[i][j]

    return a1