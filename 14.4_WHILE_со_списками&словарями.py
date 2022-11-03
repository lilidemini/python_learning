# ПРИМЕР 1.
# список пользователей, которые нужно проверить:
users = ['alice', 'brian', 'candace']

# пустой список для хранения проверенных пользователей
confirmed_users = []

# проверяем пользователей в users, пока остаются непроверенные.
# проверенные пользователи перемещаются в confirmed_users
while users:
    user = users.pop()
    print(f"{user} is verifying") # candace is verifying brian is verifying alice is verifying
    confirmed_users.append(user)

# вывод проверенных пользователей
for confirmed_user in confirmed_users:
    print(confirmed_user) # candace brian alice

# ПРИМЕР 2.
# удаление всех вхождений конкретного значения cat в списке pets
pets = ["cat", 'dog', 'cat', 'rabbit', 'fish', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets) # ['dog', 'rabbit', 'fish']

# ПРИМЕР 3.
# заполнение словаря данными, введенными пользователем
responses = {}

# установка флага на продолжение опроса
polling_active = True
while polling_active:
    name = input("Enter your name: ")
    response = input('How are you feeling today? ')

# Ответ сохраняется в словаре
    responses[name] = response

# проверка продолжения опроса
    repeat = input('Would you add your mood? yes \ no ')

    if repeat == 'no':
        polling_active = False
# опрос завершен

# выведем результаты опроса:
print('---Poll results---')
for name, response in responses.items():
    print(f"{name}`s mood for today is: {response}")

# Упражнение 7.8 стр. 142
pizza_orders = ['pepperoni', 'four_seasons', 'mozarella', 'mushrooms']

finished_pizzas = []

while pizza_orders:
    pizza_order = pizza_orders.pop()
    print(f"{pizza_order} is cooking")
    finished_pizzas.append(pizza_order)

for finished_pizza in finished_pizzas:
    print(finished_pizza)

# Упражнение 7.9 стр. 142
pizzas = ['pepperoni', 'four_seasons','pepperoni', 'mozarella', 'mushrooms', 'pepperoni']

message = 'Pepperoni not cooking'

while 'pepperoni' in pizzas:
    print(message)
    pizzas.remove('pepperoni')

print(pizzas)

# Упражнение 7.10 стр. 142

dict = {}
Polling_continue = True
while Polling_continue:
    name = input('Enter U name: ')
    city = input('Enter U city: ')
    dict[name] = city

    message = input('Do U want to continue? y \ n')
    if message == 'n':
        Polling_continue = False

print(dict)
