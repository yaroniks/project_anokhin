# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов. Посчитать
# полученные строки в каждом файле.

import re


def get_numbers_from_file(file_path: str) -> tuple[list, list]:
    """Возвращает два списка 1 - корректные 2 - некорректные"""
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()

    pattern = re.compile(r'\d{11}')
    correct_numbers = [
        pattern.search(i).group() for i in lines if pattern.search(i)
    ]

    incorrect_numbers = [
        # re.search(r'\d.+', i).group() for i in lines if re.search(r'\d.+', i)
    ]

    return correct_numbers, incorrect_numbers


print(get_numbers_from_file('hotline.txt'))
