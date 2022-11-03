# СЛОВАРИ - совокупность пар "ключ-значение"
# каждый ключ связан с некоторым значением, можно получить значение, связанное с ключом
# значение может быть: число, строка, список и другой словарь

# простейший словарь,
# где строка "color" - ключ в словаре, с которым связано значение "green"
alien_0 = {'color': 'green'}

# количество пар "ключ-значение" не ограничено
alien_0 = {'color': 'green', 'point': 5}

# ПОЛУЧИТЬ ЗНАЧЕНИЕ, связанное с ключом: указать имя словаря, затем ключ в квадратных скобках
print(alien_0['color']) # green
print(alien_0['point']) # 5

new_points = alien_0['point']
print(f"You earned {new_points}") # You earned 5

# ДОБАВЛЕНИЕ НОВЫХ ПАР "ключ-значение"
alien_0['age'] = 18
alien_0['name'] = 'Lili'
print(alien_0) #{'color': 'green', 'point': 5, 'age': 18, 'name': 'Lili'}

# СОЗДАНИЕ ПУСТОГО СЛОВАРЯ
alien_1 = {}
alien_1['color'] = 'red'
alien_1['point'] = '3'
print(alien_1) # {'color': 'red', 'point': '3'}

# ИЗМЕНЕНИЕ ЗНАЧЕНИЙ в словаре
print(f"The alien is {alien_1['color']}") # The alien is red

alien_1['color'] = 'yellow'
print(f"Now alien is {alien_1['color']}") # Now alien is yellow

# пример
alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position is {alien_3['x_position']}") # Original position is 0

# пришелец перемещается вправо
# вычисляем величину смещения на основании текущей скорости
if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3

# Новая позиция равна сумме старой и новой позиций:
alien_3['x_position'] = alien_3['x_position'] + x_increment

print(f"New position is {alien_3['x_position']}") # New position is 2


# УДАЛЕНИЕ ПАР "ключ-значение"
# удаленную пару "ключ-значение" не восстановить
alien_4 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_4) # {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

del alien_4['x_position']
print(alien_4) # {'y_position': 25, 'speed': 'medium'}

# GET - метод для назначения значения по-умолчанию
alien_5 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_5.get('points', 'No point')) # No point
print(alien_5.get('points')) # None

# добавим ключ point со значением
alien_5['points'] = 10
print(alien_5.get('points', 'No point')) #10

# упражнение 6.1 стр 113
date = {}
date['name'] = 'Lili'
date['surname'] = 'Yagya'
date['age'] = 28
date['city'] = 'Kazan'
print(date) # {'name': 'Lili', 'surname': 'Yagya', 'age': 28, 'city': 'Kazan'}

# упражнение 6.2 стр 113
favourite_numbers = {'my': 9, 'father': 13, 'Yasmin':7}
print(favourite_numbers) # {'my': 9, 'father': 13, 'Yasmin': 7}
print(favourite_numbers['my']) # 9

# ПЕРЕБОР "КЛЮЧ-ЗНАЧЕНИЕ" В СЛОВАРЕ
user_0 = {
    'username': 'lilidemini',
    'first': 'Lilia',
    'last': 'Yagyaeva'
}

# переберем ключ и значение из словаря выше
for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value:{value}')

# или
for k, v in user_0.items():
    print(f'\nKey:{k} \nValue:{v}') # Key:username Value:lilidemini Key:first Value:Lilia Key:last Value:Yagyaeva

# ПЕРЕБОР "КЛЮЧЕЙ" В СЛОВАРЕ
for k in user_0.keys():
    print(f'Key:{k}') # Key:username Key:first Key:last

# или
for k in user_0:
    print(f'Key:{k}') # Key:username Key:first Key:last
# .keys() и так используется по-умолчанию, можно указывать для улучшения читабельности кода

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['jen', 'lili']

for name in favourite_languages.keys():
    print(f'{name}')
    if name in friends:
        language = favourite_languages[name].title()
        print(f'{name.title()} loves {language}') # Jen loves Python
    else:
        print(f"Hi, {name.title()}!")

# Проверка включения ключа в словаре:
name_1 = 'phil'
if name_1 not in favourite_languages.keys():
    print(f'{name_1.title()},choose favourite language')
else:
    language = favourite_languages[name].title()
    print(f'{name_1.title()} chose {language}')

# Сортировка ключей по алфавиту
for name in sorted(favourite_languages.keys()):
    print(name) # edward jen phil sarah

# ПЕРЕБОР "ЗНАЧЕНИЙ" В СЛОВАРЕ
# values - метод для получения списка значений без ключей

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print('\nThis language was chosen:') # This language was chosen:
for language in favourite_languages.values():
    print(language.title()) # Python C Ruby Python

# set() для получения уникальных элементов списка без учета дубликатов
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print('\nThis language was chosen:') # This language was chosen:
for language in set(favourite_languages.values()):
    print(language.title()) # C Ruby Python

# упражнение 6.5 стр 120
capitals = {
    'Russia': 'Moscow',
    'USA': 'Washington',
    'China': 'Pekin',
    'Turkey': 'Ankara'
}
for k,v in capitals.items():
    print(f"{v} is the capital of {k}")

# упражнение 6.6 стр 120
countries = {
    'jen': 'Russia',
    'sarah': 'USA',
    'edward': 'China',
    'phil': 'Turkey'
}
tourists = ['lili', 'jen', 'sarah', 'tanya', 'phil']
for tourist in countries.keys():
    if tourist in tourists:
        country = countries[name]
        print(f"{tourist.title()} visited {country}")
    else:
        print(f"{tourist.title()} isn`t tourist")