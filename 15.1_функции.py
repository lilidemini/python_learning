# ПЕРЕДАЧА СПИСКА
def greeting_users(names):
    for name in names:
        print(f"Hello,{name}")

usernames = ['Lola', 'Lili', 'Kate']
greeting_users(usernames) # Hello,Lola Hello,Lili Hello,Kate


# ИЗМЕНЕНИЕ СПИСКА В ФУНКЦИИ

# функция, которая перемещает каждую модель в пустой список
def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printed model: {current_design}")
        completed_models.append(current_design)

# функция, которая выводит список напечатанных моделей
def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)

# список ненапечатнных моделей
unprinted_design = ['phone', 'robot', 'cat']

# список напечатнных моделей
completed_models = []

print_models(unprinted_design,completed_models) #Printed model: cat Printed model: robot Printed model: phone
show_completed_models(completed_models) # cat robot phone

# ЗАПРЕТ ИЗМЕНЕНИЯ СПИСКА В ФУНКЦИИ
# для этого используем копию списка [:]
print_models(unprinted_design[:],completed_models) #Printed model: cat Printed model: robot Printed model: phone
show_completed_models(completed_models)

# Упражнение 8.9 стр 160
messages = ['Hello', 'Thank you', 'See you', 'Goodbye']

def greeting(message):
    for message in messages:
        print(message)

greeting(messages) # Hello Thank you See you Goodbye

# Упражнение 8.10 стр 160
def send_message(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"'{current_message}' is sending")
        sent_messages.append(current_message)

def show_messages(message, sent_messages):
    print(message)
    print(sent_messages)

messages = ['Hello', 'Thank you', 'See you', 'Goodbye']
sent_messages = []

send_message(messages, sent_messages) # 'Goodbye' is sending 'See you' is sending 'Thank you' is sending 'Hello' is sending
show_messages(messages, sent_messages) # [] ['Goodbye', 'See you', 'Thank you', 'Hello']

# Упражнение 8.11 стр 160
def send_message(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"'{current_message}' is sending")
        sent_messages.append(current_message)

def show_messages(message, sent_messages):
    print(message)
    print(sent_messages)

messages = ['Hello', 'Thank you', 'See you', 'Goodbye']
sent_messages = []

send_message(messages[:], sent_messages) # 'Goodbye' is sending 'See you' is sending 'Thank you' is sending 'Hello' is sending
show_messages(messages, sent_messages) # ['Hello', 'Thank you', 'See you', 'Goodbye'] ['Goodbye', 'See you', 'Thank you', 'Hello']

# ПРОИЗВОЛЬНЫЙ НАБОР АРГУМЕНТОВ *args
def pizza(*toppings):
    print(toppings)

pizza('margarita') # ('margarita',)
pizza('pepperoni', 'margarita', 'cheeze') # ('pepperoni', 'margarita', 'cheeze')

# перебор списка:
def pizza(*toppings):
    for topping in toppings:
        print(topping)

pizza('margarita') # margarita
pizza('pepperoni', 'margarita', 'cheeze') # pepperoni, margarita, cheeze

# Позиционные аргументы с произвольными
# параметр для получения произвольных элементов должен стоять на последнем месте
def pizza(size, *toppings):
    print(f"We can make {size}sm pizzas:")
    for topping in toppings:
        print(topping)

pizza(32, 'pepperoni', 'margarita', 'cheeze') # We can make 32sm pizzas: pepperoni margarita cheeze

# ПРОИЗВОЛЬНЫЕ ИМЕНОВАННЫЕ АРГУМЕНТЫ **kwargs
def create_profile(name, surname, **user_info):
    user_info['first_name'] = name.title()
    user_info['last_name'] = surname.title()
    return user_info

user = create_profile('lili', 'demini', city='Kazan', birth=1994)
print(user) # {'city': 'Kazan', 'birth': 1994, 'first_name': 'Lili', 'last_name': 'Demini'}

