# Создать словарь из списков keys = ['Ten', 'Twenty', 'Thirty'] и values = [10, 20, 30].

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
output = {}

for idx, key in enumerate(keys):
    output[key] = values[idx]

print(output)
