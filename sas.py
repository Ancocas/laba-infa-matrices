import matrix

a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
b = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
A = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]

print("Сумма матриц a и b =", matrix.sum_matrices(a, b))
print("Произведение матрицы a и b =", matrix.prod_matrix_scalar(a, b))
print("Транспонированная матрица a =", matrix.transposed_matrix(a))
print("Обратная матрица a =", matrix.reversed_matrix(A))
print("Определитель матрицы A =", matrix.determinant(a))
