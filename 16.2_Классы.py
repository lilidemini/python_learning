class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_car = Car('audi', 'a4', 2022)
print(my_car.get_descriptive_name()) # 2022 Audi A4

# Назначение атрибуту значение по-умолчанию
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # добавили значение по умолчанию

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

my_car = Car('KIA', 'optima', 2019)
my_car.read_odometer() # This car has 0 miles on it

my_car.odometer_reading = 25
my_car.read_odometer() # This car has 25 miles on it

# Изменение значения атрибута с использованием метода
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # добавили значение по умолчанию

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    # новый метод для изменения показаний одометра:
    def update_read_odometer(self, mileage):
        self.odometer_reading = mileage

my_car = Car('KIA', 'optima', 2019)
my_car.update_read_odometer(55)
my_car.read_odometer() # This car has 55 miles on it

# Изменение значения атрибута с приращением
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # добавили значение по умолчанию

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    # метод для изменения показаний одометра:
    def update_read_odometer(self, mileage):
        self.odometer_reading = mileage

    #  метод для приращения показаний одометра:
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_used_car = Car('KIA', 'optima', 2019)

my_used_car.update_read_odometer(23_500)
my_used_car.read_odometer() # This car has 23500 miles on it

my_used_car.increment_odometer(100)
my_used_car.read_odometer() # This car has 23600 miles on it

# Упражнение 9.4 стр. 180
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def get_number_served(self):
        print(f"{self.number_served} guests was surved in {self.restaurant_name}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, numbers):
        self.number_served += numbers

restaurant = Restaurant('Sushi', 'Chinese')
restaurant.get_number_served() # 0 guests was surved in Sushi

restaurant.number_served = 11
restaurant.get_number_served() # 11 guests was surved in Sushi

restaurant.set_number_served(23)
restaurant.get_number_served() # 23 guests was surved in Sushi

restaurant.increment_number_served(10)
restaurant.get_number_served() # 33 guests was surved in Sushi
