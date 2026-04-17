# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.

import random


def print_matrix(matrix: list[list[int]]):
    for i in matrix:
        print(*i)


def generate_matrix(n: int) -> list[list[int]]:
    return [
        [random.randint(5, 5) for j in range(n)]
        for i in range(n)
    ]


def change_main_diagonal(matrix: list[list[int]]) -> list[list[int]]:
    return [
        [matrix[i][j]*2 if i == j else matrix[i][j] for j in range(len(matrix))]
        for i in range(len(matrix))
    ]


n = int(input("Введите размер матрицы: "))
matrix = generate_matrix(n)

print('Исходная матрица:')
print_matrix(matrix)

matrix = change_main_diagonal(matrix)

print('\nГлавная диагональ увеличеная в 2 раза:')
print_matrix(matrix)
