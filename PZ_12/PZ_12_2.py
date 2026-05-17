# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.

import random
from functools import reduce


def print_matrix(matrix: list[list[int]]):
    for i in matrix:
        print(*i)


def generate_matrix(n: int) -> list[list[int]]:
    return [
        [random.randint(-5, 5) for j in range(n)]
        for i in range(n)
    ]


def sum_avg_matrix(matrix: list[list[int]]) -> tuple[list[int], int, float]:
    nums = list(filter(
        lambda j: j > 0 and j % 2 == 0,
        reduce(lambda x, y: x+y, matrix)
    ))
    return nums, sum(nums), sum(nums) / len(nums)


n = int(input("Введите размер матрицы: "))
matrix = generate_matrix(n)

print('Исходная матрица:')
print_matrix(matrix)

nums, nums_sum, nums_avg = sum_avg_matrix(matrix)
print(f'\nМассив из положительных четных элементов: {nums}')
print(f'Сумма: {nums_sum}')
print(f'Среднее арифметическое: {nums_avg}')
