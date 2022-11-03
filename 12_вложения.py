# Вложение - сложные структуры из множества словарей в списке или список как значение элемента в словаре
alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2] # [{'color': 'green', 'point': 5}, {'color': 'yellow', 'point': 10}, {'color': 'red', 'point': 15}]
print(aliens)

# создание пустого списка
aliens = []

# создание 30 зеленых пришельцев
for alien_number in range(10):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens) # [{'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}]

# вывод первых 5 пришельцев:
print(aliens[:5])

# или
for alien in aliens[:5]:
    print(aliens)

# вывод количества созданных пришельцев:
print(f"Total number of aliens: {len(aliens)}") # Total number of aliens: 10 aliens

# изменим цвет и скорость у первых трех пришельцев:
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        print(aliens[:5]) #  [{'color': 'red', 'point': 5, 'speed': 'fast'}, {'color': 'red', 'point': 5, 'speed': 'fast'}, {'color': 'red', 'point': 5, 'speed': 'fast'}, {'color': 'green', 'point': 5, 'speed': 'slow'}, {'color': 'green', 'point': 5, 'speed': 'slow'}]

# СПИСОК В СЛОВАРЕ
clothes = {
    'type': 'hat',
    'composition': ['50% cotton', '50% poliester']
}
print(f"Your {clothes['type']} consist of:") # Your hat consist of:

for i in clothes['composition']:
    print('\t' + i) # 	50% cotton	50% poliester

# Пример:
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'java']
}

for name, languages in favourite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}`s favourite languages is:")
    else:
        print(f"{name.title()}`s favourite language are:")
    for language in languages:
        print(f"\t" + language)

# СЛОВАРЬ В СЛОВАРЕ
users = {
    'LiliaY':{
        'first': 'Lilia',
        'last': 'Yagyaeva',
        'age': 28
    },
    'IlyasY':{
        'first': 'Ilyas',
        'last': 'Yagyaev',
        'age': 31
    }
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    fullName = f"{userinfo['first']} {userinfo['last']}"
    age = userinfo['age']
    print(f"\tFull name: {fullName}")
    print(f"\tAge: {age}")

# Упражнение 6.7 стр.126
LiliaY = {
        'first': 'Lilia',
        'last': 'Yagyaeva',
        'age': 28
}
IlyasY = {
    'first': 'Ilyas',
    'last': 'Yagyaev',
    'age': 31
}
YasminaY = {
    'first': 'Yasmina',
    'last': 'Yagyaeva',
    'age': 7
}

# сохраним выше словари в списке people
people = [LiliaY, IlyasY, YasminaY]
print(people)# [{'first': 'Lilia', 'last': 'Yagyaeva', 'age': 28}, {'first': 'Ilyas', 'last': 'Yagyaev', 'age': 31}, {'first': 'Yasmina', 'last': 'Yagyaeva', 'age': 7}]

for i in people:
    print(i)