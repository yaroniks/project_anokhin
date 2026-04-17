# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.

import random


def print_matrix(matrix: list[list[int]]):
    for i in matrix:
        print(*i)


def generate_matrix(n: int) -> list[list[int]]:
    return [
        [random.randint(-100, 100) for j in range(n)]
        for i in range(n)
    ]


def sum_avg_matrix(matrix: list[list[int]]) -> tuple[list[int], int, float]:
    nums = []
    for i in matrix:  # i - строка
        for j in i:  # j - стобец
            if j > 0 and j % 2 == 0:
                nums.append(j)
    return nums, sum(nums), sum(nums) / len(nums)


n = int(input("Введите размер матрицы: "))
matrix = generate_matrix(n)

print('Исходная матрица:')
print_matrix(matrix)

nums, nums_sum, nums_avg = sum_avg_matrix(matrix)
print(f'\nМассив из положительных четных элементов: {nums}')
print(f'Сумма: {nums_sum}')
print(f'Среднее арифметическое: {nums_avg}')
