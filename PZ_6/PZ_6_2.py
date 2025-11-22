# Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).

import random

try:
    n = int(input("Введите размер списка: "))
except ValueError:
    print('Введите число')
    exit()


def find_minimum(nums: list[int]) -> int:
    minimum = None
    for i in range(1, len(nums) - 1):
        if nums[i-1] > nums[i] < nums[i+1]:
            minimum = nums[i]

    if nums[0] < nums[1] and nums[0] < minimum:
        return nums[0]

    if nums[-1] < nums[-2] and nums[-1] < minimum:
        return nums[-1]

    return minimum


nums = [random.randint(0, 100) for i in range(n)]
print(nums)
print(f'Локальный минимум: {find_minimum(nums)}')
