# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов. Посчитать
# полученные строки в каждом файле.

import re


def get_numbers_from_file(file_path: str, correct_filepath: str = './1.txt', incorrect_filepath: str = './2.txt') -> tuple[list, list]:
    """Возвращает два списка 1 - корректные 2 - некорректные"""
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()

    numbers = [match.group() for i in lines if (match := re.search(r'\d+', i))]
    correct_numbers = [n for n in numbers if len(n) == 11]
    incorrect_numbers = [n for n in numbers if len(n) != 11]

    with open(correct_filepath, 'w', encoding='utf-8') as file:
        file.write('\n'.join(correct_numbers))
    with open(incorrect_filepath, 'w', encoding='utf-8') as file:
        file.write('\n'.join(incorrect_numbers))

    return correct_numbers, incorrect_numbers


currect, incurrect = get_numbers_from_file('./hotline.txt')
print(currect, len(currect))
print(incurrect, len(incurrect))
