# Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).

try:
    n = int(input("Введите размер списка: "))
    nums = [int(input(f'Введите {i} элемент списка: ')) for i in range(n)]
except ValueError:
    print('Введите число')
    exit()


def find_minimum(nums: list[int]) -> int:
    if len(nums) == 2 or len(nums) == 3:
        if nums[0] < nums[1]:
            return nums[0]
        if nums[-1] < nums[-2]:
            return nums[-1]

    for i in range(1, len(nums) - 1):
        if nums[i-1] > nums[i] < nums[i+1]:
            return nums[i]


print(f'Локальный минимум: {find_minimum(nums)}')
