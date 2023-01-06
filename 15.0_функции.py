# ФУНКЦИЯ - именованный блок кода, предназначенный для решения одной конкретной задачи.
# Вместо того, чтобы дублировать код, происходит вызов функции для выполнения кода внутри функции.

# простая функция с именем greet_user(), которая выводит приветсвие:
def greet_user():
    '''Выводит простое приветсвие'''
    print('Hello!')

# вызывали функцию
greet_user() # Hello!

# пример 1: перемнная username - параметр, а значение "Lili" - аргумент
def greet_user(username):
    print(f"Hello, {username}")

greet_user("Lili") # Hello, Lili

# Упражнение 8.1 стр 145
def display_message():
    print('Функции')

display_message() # Функции

# Упражнение 8.2 стр 145
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book('Alice in Wonderland') # One of my favorite books is Alice in Wonderland

# ПОЗИЦИОННЫЕ АРГУМЕНТЫ перечисляются в порядке соответсвующем порядку записи параметров
def describe_pet(animal_type, pet_name):
    '''Выводит инфу о животном'''
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name}.")

describe_pet('fish', 'Nemo') # I have a fish. My fish`s name is Nemo.
describe_pet('dog', 'Pyffi') # I have a dog. My dog`s name is Pyffi.


# ИМЕНОВАННЫЕ АРГУМЕНТЫ - пара имя-значение
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name}.")

describe_pet(animal_type='cat', pet_name='Mysya') # I have a cat. My cat`s name is Mysya.
describe_pet(pet_name='Mysya', animal_type='cat') # I have a cat. My cat`s name is Mysya.

# ЗНАЧЕНИЯ ПО-УМОЛЧАНИЮ
def describe_pet(pet_name, animal_type = 'dog'):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name}.")

describe_pet('Sharik') # I have a dog. My dog`s name is Sharik.
describe_pet(pet_name = 'Sharik') # # I have a dog. My dog`s name is Sharik.

describe_pet('Nemo', 'fish') # I have a fish. My fish`s name is Nemo.
describe_pet(pet_name = 'Nemo', animal_type = 'fish') # I have a fish. My fish`s name is Nemo.

# Упражнение 8.3 стр 150
def make_shirt(size, text):
    print(f"The size of shirt: {size}.")
    print(f"The text on shirt is: {text}.")

make_shirt('S', 'I`m free') # The size of shirt: S. The text on shirt is: I`m free.
make_shirt(text='I`m free', size='S') # The size of shirt: S. The text on shirt is: I`m free.

# Упражнение 8.4 стр 150
def make_shirt(size = 'L', text = 'I love Python'):
    print(f"The size of shirt: {size}.")
    print(f"The text on shirt is: {text}.")

make_shirt() #The size of shirt: L. The text on shirt is: I love Python.

# НЕОБЯЗАТЕЛЬНЫЕ АРГУМЕНТЫ
# пример с необязательным аргументом  middle_name, для этого присвоим ему пустое значение
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician) # Jimi Hendrix

musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician) # Jimi Lee Hendrix

# Возвращение словаря
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician) # {'first': 'jimi', 'last': 'hendrix'}

# пример с необязательным параметром Age со значением по-умолчанию None
# при проверке None интерпретируется как False
def build_person(first_name, last_name, age = None):
    person = {"name": first_name, "surname": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person('jimi', 'hedrix', age=66)
print(musician) # {'name': 'jimi', 'surname': 'hedrix', 'age': 66}

musician = build_person('jimi', 'hedrix')
print(musician) # {'name': 'jimi', 'surname': 'hedrix'}

# Упражнение 8.6 стр 156
def city_country(city, country):
    message = f"{city}, {country}"
    return message

print(city_country('Kazan', 'Russia')) # Kazan, Russia

# Упражнение 8.7 и 8.8 стр 156
def make_album(author_name, album_name, number = None):
    dict = {'author': author_name, 'album': album_name}

    if number:
        dict['number'] = number
    return dict

print(make_album('имя автора', 'альбом автора')) # {'author': 'имя автора', 'album': 'альбом автора'}

while True:
    auth_name = input('Введите имя автора: ')
    if auth_name == 'q':
        break

    al_name = input('Введите название альбома: ')
    if al_name == 'q':
        break

    number = input('Введите количество дорожек: ')
    if number == 'q':
        break

    album = make_album(auth_name, al_name, number)
    print(album)

