# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.

from datetime import date


class Car:
    def __init__(self, name: str, model: str, release: date):
        self.name: str = name
        self.model: str = model
        self.date: date = release


class Truck(Car):
    def __init__(self, name: str, model: str, release: date, load: int):
        super().__init__(name, model, release)
        self.load = load


class PassengerCar(Car):
    def __init__(self, name: str, model: str, release: date, passangers: int):
        super().__init__(name, model, release)
        self.passangers = passangers


car = Car('машина', 'модель', date.today())
truck = Truck('MAN', 'MAN', date.today(), 5000)
bmw = PassengerCar('BMW', 'X5', date.today(), 4)
