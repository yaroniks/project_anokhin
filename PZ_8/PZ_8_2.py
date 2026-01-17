# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16', отражающая
# продажи продукции по дням в кг. Преобразовать информацию из строки в словари,
# с использованием функции найти максимальные продажи по каждому виду
# продукции, результаты вывести на экран.

def find_max_sales(sales: list[int]) -> int:
    return max(sales)


text = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
print(text)

data = {}
product = None
for i in text.split():
    if not i.isdigit():
        product = i
        data[i] = []
    else:
        data[product].append(int(i))

print(data)
for i in data:
    print(f'Максимальные продажи по {i}: {find_max_sales(data[i])}')
