# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.

class Counter:
    def __init__(self):
        self.number = 0

    def incriment(self):
        self.number += 1

    def discriment(self):
        self.number -= 1


counter = Counter()
print(counter.number)

counter.incriment()
print(counter.number)

counter.discriment()
print(counter.number)
