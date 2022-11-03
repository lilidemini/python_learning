# 4. СПИСКИ
friends = ['kate', "sasha", 'irina', 'yana']
print(friends[0].title()) #Kate
print(friends[-1]) #yana

message_for_Kate = f'My best schoolfriend is {friends[0].title()}'
print(message_for_Kate)

# Замена элементов в списке
cars = ['LADA', 'daewoo', 'skoda', 'KIA']
print(cars) #['LADA', 'daewoo', 'skoda', 'KIA']

cars[0] = 'Hyundai'
print(cars) #['Hyundai', 'daewoo', 'skoda', 'KIA']

# Добавление элементов в список
# способ 1. метод append() для присоединение элементов в конец списка
friends.append('Alina')
print(friends) #['kate', 'sasha', 'irina', 'yana', 'Alina']

# способ 2.  метод insert() для вставки элементов в список в произвольную позицию
friends.insert(2, 'Zarina')
print(friends) #['kate', 'sasha', 'Zarina', 'irina', 'yana', 'Alina']

# Удаление элементов в списке
# способ 1. команда del удаляет элемент по индексу навсегда
del friends[2]
print(friends) #['kate', 'sasha', 'irina', 'yana', 'Alina']

# способ 2. метод pop() удаляет последний элемент списка, но хранит его для дальнейшего использования
popped_friends = friends.pop()
print(friends) #['kate', 'sasha', 'irina', 'yana']
print(popped_friends) #Alina

# способ 3. метод pop() извлекает по индексу элемент списка и хранит его для дальнейшего использования
first_friend = friends.pop(1)
print(friends) #['kate', 'irina', 'yana']
print(first_friend) #sasha
print(f'My first friend was {first_friend.title()}') #My first friend was Sasha

# способ 4. метод remove() для удаления по значению
friends.remove('irina')
print(friends) #['kate', 'yana']

not_friend = 'yana'
friends.remove(not_friend)
print(f'My truly friend is {friends[0]}') #My truly friend is kate
# метод удаляет первое попавшееся соответствующее значение. для удаления всех других аналогичных значений - используй цикл

# Упорядочение списка
# способ 1: метод sort() для постоянной сортировки, нет возврата к исходному неосортированному списку
homies = ['kate', 'sasha', 'Ирина', 'Яна', 'Alina']
homies.sort() # сортировка в алфавитном порядке
print(homies) #['Alina', 'kate', 'sasha', 'Ирина', 'Яна']

homies.sort(reverse=True) # сортировка в обратном алфавитном порядке
print(homies) # ['Яна', 'Ирина', 'sasha', 'kate', 'Alina']

# способ 2: метод sorted() для временной сортировки
homies = ['kate', 'sasha', 'Ирина', 'Яна', 'Alina']

print('This is original list:')
print(homies) #['kate', 'sasha', 'Ирина', 'Яна', 'Alina']

print('\nThis is sorted list:')
print(sorted(homies)) #['Alina', 'kate', 'sasha', 'Ирина', 'Яна']

print('\nThis is reverse sorted list:') #сортировка в обратном алфавитном порядке
print(sorted(homies, reverse=True)) #['Яна', 'Ирина', 'sasha', 'kate', 'Alina']

print('\nThis is original list again:')
print(homies) #['kate', 'sasha', 'Ирина', 'Яна', 'Alina']

# Вывод списка в обратном порядке без сортировки - метод reverse()
cars = ['LADA', 'daewoo', 'skoda', 'KIA']
cars.reverse()
print(cars) #['KIA', 'skoda', 'daewoo', 'LADA']

# Определить длину списка - функция len()
print(len(cars)) # 4

#Упражнение 3.4 стр.58
guests = ['ильяс', "Зинур", "саша", "яна", "Катя"]
print(f'Привет, {guests[0].title()}! \nЖду тебя на своем ДР\n')
print(f'Привет, {guests[1].title()}! \nЖду тебя на своем ДР\n')
print(f'Привет, {guests[2].title()}! \nЖду тебя на своем ДР\n')
print(f'Привет, {guests[3].title()}! \nЖду тебя на своем ДР\n')
print(f'Привет, {guests[4].title()}! \nЖду тебя на своем ДР\n')

#Упражнение 3.5 стр.58
print(f'{guests[4]} не сможет прийти на мой ДР')
guests[4]=  "Алина"
print(guests) #['ильяс', 'Зинур', 'саша', 'яна', 'Алина', 'Ирина']

#Упражнение 3.6 стр.58
guests.insert(0, 'Ирина') # добавление в начало списка
print(guests) #['Ирина', 'ильяс', 'Зинур', 'саша', 'яна', 'Алина']

guests.insert(3, 'Катерина') # добавление в середину списка
print(guests) #['Ирина', 'ильяс', 'Зинур', 'Катерина', 'саша', 'яна', 'Алина']

guests.append('Yasmin') #добавление в конец
print(guests) #['Ирина', 'ильяс', 'Зинур', 'Катерина', 'саша', 'яна', 'Алина', 'Yasmin']

#Упражнение 3.7 стр.58
print(f'К сожалению на ДР приглашаются только два гостя: {guests[1].title()} и {guests[-1].title()}') #К сожалению на ДР приглашаются только два гостя: Ильяс и Yasmin

print(f'Извини, {guests.pop(0)} , но я мое ДР отменяется') #Извини, Ирина , но я мое ДР отменяется
print(guests) #['ильяс', 'Зинур', 'Катерина', 'саша', 'яна', 'Алина', 'Yasmin']

print(f'Извини, {guests.pop(1)} , но я мое ДР отменяется') #Извини, Зинур , но я мое ДР отменяется
print(guests) #['ильяс', 'Катерина', 'саша', 'яна', 'Алина', 'Yasmin']

print(f'Извини, {guests.pop(1)} , но я мое ДР отменяется') # Извини, Катерина , но я мое ДР отменяется
print(guests)#['ильяс', 'саша', 'яна', 'Алина', 'Yasmin']

print(f'Извини, {guests.pop(1)} , но я мое ДР отменяется') # Извини, саша , но я мое ДР отменяется
print(guests)#['ильяс', 'яна', 'Алина', 'Yasmin']

print(f'Извини, {guests.pop(1)} , но я мое ДР отменяется') # Извини, яна , но я мое ДР отменяется
print(guests)#['ильяс', 'Алина', 'Yasmin']

print(f'Извини, {guests.pop(1)} , но я мое ДР отменяется') # Извини, Алина , но я мое ДР отменяется
print(guests)#['ильяс', 'Yasmin']

del guests[0]
print(guests)#['Yasmin']

del guests[0]
print(guests)#пустой список []


#Упражнение 3.8 стр.61
countries = ['China', 'Russia', 'Ukraine', 'Germany', 'USA']

print(sorted(countries)) # ['China', 'Germany', 'Russia', 'USA', 'Ukraine']
print(countries) # ['China', 'Russia', 'Ukraine', 'Germany', 'USA']

print(sorted(countries, reverse=True)) #['Ukraine', 'USA', 'Russia', 'Germany', 'China']
print(countries) # ['China', 'Russia', 'Ukraine', 'Germany', 'USA']

countries.reverse()
print(countries) # ['USA', 'Germany', 'Ukraine', 'Russia', 'China']

countries.reverse()
print(countries) # ['China', 'Russia', 'Ukraine', 'Germany', 'USA']

countries.sort()
print(countries) #['China', 'Germany', 'Russia', 'USA', 'Ukraine']

print(len(countries)) # 5
