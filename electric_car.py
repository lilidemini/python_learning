# импортирование модуля в модуль
from cars import Car

class Battery():
    def __init__(self, battery_size=55):
        self.battery_size = battery_size

    def describe_battery(self): # определим метод
        print(f"This car has {self.battery_size}-kW battery")

    def get_range(self):
        if self.battery_size == 55:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    def __init__(self, make, model, year): # инициализирует атрибуты родительского класса
        super().__init__(make, model, year) # инициализирует атрибуты класса потомка
        self.battery = Battery() # определим атрибут как класс