# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.

import random

try:
    n = int(input('Введите количество элементов: '))
except ValueError:
    print('Введите число.')
    exit()

spisok = [random.randint(0, 100) for i in range(n)]

print(spisok)
crat_tri = [i for i in spisok if i % 3 == 0]
ne_crat_tri = [i for i in spisok if i % 3 != 0]

print(f'\nЧисла, кратные трём: {crat_tri}\nКоличество элементов: {len(crat_tri)}\n')
print(f'Все остальные числа: {ne_crat_tri}\nКоличество элементов: {len(ne_crat_tri)}')
