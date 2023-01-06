# синтаксис:
# class название_класса:
#   атрибуты_класса
#   методы_класса

# создадим класс Dog
class Dog():

    # инициализируем атрибуты name и  age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # методы sit и roll_over
    def sit(self):
        print(f"{self.name} is sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")

# создадим экземпляр, представляющий кокретную собаку
my_dog = Dog('Puffi', 1)

print(f"My dog`s name is {my_dog.name}") # My dog`s name is Puffi
print(f"My dog is {my_dog.age} years old") # My dog is 1 years old

# вызовим  методы, определенные в Dog, после создания экземпляра
my_dog.sit() # Puffi is sitting
my_dog.roll_over() # Puffi rolled over!

# Упражнение 9.1 стр.175
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}`s chef is cooking {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

italy = Restaurant('Italiano', 'Italian')
italy.describe_restaurant() # Italiano`s chef is cooking Italian cuisine
italy.open_restaurant() # Italiano is open!

# Упражнение 9.2 стр.175
china = Restaurant('Sushi', 'Chinese')
greece = Restaurant('Giros', 'Greek')

china.describe_restaurant() # Sushi`s chef is cooking Chinese cuisine
greece.describe_restaurant() # Giros`s chef is cooking Greek cuisine


# Упражнение 9.3 стр.175
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

Lili = User('Lilia', 'Yagya', 28, 'lilidemini')
Ilyas = User('Ilyas', 'Yagya', 30, 'ezozes')
print(Lili.describe_user()) # Lilia Yagya 28 lilidemini
Ilyas.greet_user() # Hello, Ilyas Yagya


