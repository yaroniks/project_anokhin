# Дан список размера N (N — четное число). Поменять местами его первый элемент
# со вторым, третий — с четвертым и т. д.

try:
    n = int(input('Введите размер списка: '))
except ValueError:
    print('Введите число')
    exit()

if n % 2 != 0:
    print('Число должно быть чётным')
    exit()

spisok = list(range(n))
print(spisok)

for i in range(0, len(spisok), 2):
    # spisok[i], spisok[i+1] = spisok[i+1], spisok[i]
    now = spisok[i]
    spisok[i] = spisok[i+1]
    spisok[i+1] = now

print(spisok)
