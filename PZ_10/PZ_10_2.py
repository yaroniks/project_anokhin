# Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы третей
# строки их числовыми кодами.

import string

with open('text18-3.txt', encoding='utf-16-le') as file:
    text = file.read()

print(text)

split = text.split('\n')
punctuation = []
for line in split[:4]:
    for char in line:
        if char in string.punctuation + '«»':
            punctuation.append(char)
print(f"\nКоличество знаков пунктуации: {len(punctuation)}")

split[2] = ''.join([str(ord(i)) for i in split[3]])
with open('new_file.txt', 'w', encoding='utf-16-le') as file:
    file.write('\n'.join(split))
