# Составить функцию, которая выполнит суммирования числового ряда.


def sum_nums(n: int):
    if n < 1:
        return 0
    return n * (n + 1) // 2


try:
    n = int(input('Введите до какого числа идёт ряд: '))
except ValueError:
    print('Введите число.')
    exit()

print(f'Сумма числово ряда от 1 до {n}: {sum_nums(n)}')
