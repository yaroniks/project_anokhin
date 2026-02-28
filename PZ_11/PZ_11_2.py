# Составить генератор (yield), который выводит из строки только цифры.

def find_numbers(text: str) -> int:
    for i in text:
        if i.isdigit():
            yield int(i)


text = input('Введите строку: ')

nums = find_numbers(text)
print(list(nums))
