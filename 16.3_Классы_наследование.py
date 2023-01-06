# исходный класс - родитель
# наследуемый класс - потомок
# потомок наследует от родителя артибуты и методы, но при этом может определять и собственные

# 1. СОЗДАНИЕ КЛАССА-ПОТОМКА
class Car(): # класс-родитель
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

# создадим класс-потомок или подкласс
class ElectricCar(Car): # класс-потомок
    def __init__(self, make, model, year):

# функция super позволяет вызвать метод класса-родителя, в результате экземпляр ElectricCar наследует атрибуты класса-родителя
        super().__init__(make, model, year)

tesla = ElectricCar('tesla', 'model S', 2010)
print(tesla.get_descriptive_name()) # 2010 Tesla Model S


# 2. ОПРЕДЕЛИМ АТРИБУТ И МЕТОД КЛАССА-ПОТОМКА
class Car(): # класс-родитель
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class ElectricCar(Car): # класс-потомок
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
# определим атрибут класса-потомка
        self.battery_size = 75

# определим метод класса-потомка
    def describe_battery(self):
        print(f"This car has {self.battery_size}-kW battery")


tesla = ElectricCar('tesla', 'model S', 2010)
print(tesla.get_descriptive_name()) # 2010 Tesla Model S
tesla.describe_battery() # This car has 75-kW battery


# 3. ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ КЛАССА-РОДИТЕЛЯ
# для этого в классе потомке определить метод с таким же именем, что и в родительском классе
class Car(): # класс-родитель
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.liters = 45 # добавили значение по умолчанию

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # метод родительского класса для переопределения в потомке ElectricCar
    def fill_gas_tank(self):
        print(f"This car need {self.liters} in a gas tank")

class ElectricCar(Car): # создали класс-потомок
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75 # определим атрибут класса-потомка

    def describe_battery(self): # определим метод класса-потомка
        print(f"This car has {self.battery_size}-kW battery")

# переопределим метод родительского класса
    def fill_gas_tank(self):
        print("This car doesn`t need a gas tank")

tesla = ElectricCar('tesla', 'model S', 2010)
tesla.fill_gas_tank() # This car doesn`t need a gas tank

# ЭКЗЕМПЛЯРЫ КАК АТРИБУТЫ
class Car(): # класс-родитель
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

# класс, котрый будет использован как атрибут другого класса
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


class ElectricCar(Car):
    def __init__(self, make, model, year): # инициализирует атрибуты родительского класса
        super().__init__(make, model, year) # инициализирует атрибуты класса потомка
        self.battery = Battery() # определим атрибут как класс

tesla = ElectricCar('Reno', 'Electro', 2022)
print(tesla.get_descriptive_name()) # 2022 Reno Electro
tesla.battery.describe_battery() # This car has 55-kW battery
tesla.battery.get_range() # This car can go about 260 miles on a full charge

# Упражнение 9.6 стр 186
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}`s chef is cooking {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['iskimo', 'shocolate', 'berries']

    def printing_flavors(self):
        for i in self.flavors:
            print(i)

shop = IceCreamStand('IceShop', '')
shop.printing_flavors() # iskimo shocolate berries

# Упражнение 9.7 стр 186
class User():
    def __init__(self, first_name, last_name, age, login):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.login = login

    def describe_user(self):
        user_info = (f"{self.name} {self.surname} {self.age} {self.login}")
        return user_info

    def greet_user(self):
        print(f"Hello, {self.name} {self.surname}")

class Admin(User):
    def __init__(self, first_name, last_name, age, login):
        super().__init__(first_name, last_name, age, login)
        self.privileges = ['delete', 'update', 'create', 'read']

    def show_privileges(self):
        for i in self.privileges:
            print(i)

Lili = Admin('Lilia', 'Yagya', 28, 'lilidemini')
Lili.show_privileges() # delete update create read

# Упражнение 9.8 стр 186
class User():
    def __init__(self, first_name, last_name, age, login):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.login = login

    def describe_user(self):
        user_info = (f"{self.name} {self.surname} {self.age} {self.login}")
        return user_info

    def greet_user(self):
        print(f"Hello, {self.name} {self.surname}")

class Privileges():
    def __init__(self):
        self.privileges = ['delete', 'update', 'create', 'read']

    def show_privileges(self):
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self, first_name, last_name, age, login):
        super().__init__(first_name, last_name, age, login)
        self.privileges = Privileges()

Lili = Admin('Lilia', 'Yagya', 28, 'lilidemini')
Lili.privileges.show_privileges() # delete update create read

# Упражнение 9.9 стр 186
class Car(): # класс-родитель
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

# класс, котрый будет использован как атрибут другого класса
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

tesla = ElectricCar('Reno', 'Electro', 2022)
print(tesla.get_descriptive_name()) # 2022 Reno Electro
tesla.battery.describe_battery() # This car has 55-kW battery
tesla.battery.get_range() # This car can go about 260 miles on a full charge
tesla.battery.upgrade_battery()
tesla.battery.get_range() # This car can go about 315 miles on a full charge

