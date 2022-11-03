# КОМАНДА IF
# age = int(input())
age = 18
if age >= 18:
    print('You`re old enought to vote')
# если возраст 18 и более, то выводится текст в принт, иначе ничего не выводится


# КОМАНДА IF-ELSE,где всегда выполняется одно из двух возможных действий
if age >= 18:
    print('You`re old enought to vote')
else:
    print('Sorry, you are young to vote')
# если возраст 18 и более, то выводится первый текст в принт, иначе второй.


# КОМАНДА IF-ELIF-ELSE,где выполняется одно из многочисленных возможных действий
# ELIF может быть сколько угодно
if age <= 7:
    print(f'{age} years old are children')
elif age <= 18:
    print(f'{age} years old are schoolchildren')
elif age <= 25:
    print(f'{age} years old are students')
elif age <= 60:
    print(f'{age} years old are workers')
else:
    print(f'{age} years old are pensioners')

# компактная версия уравнения. Результат один и тот же, но эффективность и изменяемость проще.
if age <= 7:
    people = 'children'
elif age <= 18:
    people = 'schoolchildren'
elif age <= 25:
    people = 'students'
elif age <= 60:
    people = 'workers'
else:
    people = 'pensioners'
print(f'{age} years old are {people}\n')

# ELSE - необязательный блок, если смысл кода более понятен, например как тут:
if age <= 7:
    people = 'children'
elif age <= 18:
    people = 'schoolchildren'
elif age <= 25:
    people = 'students'
elif age <= 60:
    people = 'workers'
elif age >60:
    people = 'pensioners'
print(f'{age} years old are {people}\n')

# Упражнение 5.6 на стр. 99
if age < 2:
    people = 'младенец'
elif (age >= 2) and (age < 13):
    people = 'ребенок'
elif (age >= 13) and (age < 20):
    people = 'подросток'
elif (age >= 20) and (age < 65):
    people = 'взрослый'
elif age >=65:
    people = 'пожилой'
print(f'{age} years old are {people}\n')

# Проверка наличия элементов в списке
shop_basket = ['skirt', 'jacket', 'hat', 'shoes']

# Ex.1
for item in shop_basket:
    if item == shop_basket[2]:
        print(f"Sorry, {item.lower()} isn`t available")
    else:
        print(f'{item.title()} is added to shopbasket')

# Ex.2
shop_basket = []
if shop_basket:
    for item in shop_basket:
        print(f"Adding {item} to a shop basket")
    print("Make a purchase\n")
else:
    print("Shop bascket is epmty\n") #Shop bascket is epmty

# Ex.3
available_items = ['skirt', 'jacket', 'shoes']
shop_basket = ['skirt', 'jacket', 'hat', 'shoes', 'glasses']

for item in shop_basket:
    if item in available_items:
        print(f"{item.title()} was added in shop basket\n")
    else:
        print(f'\tSorry, we can`t add {item.title()}\n')
print("Get ready to pay your items in shop basket")

# Упражнение 5.8 стр. 103
users = ['Lili', 'Iren', 'Tina', 'Ivan', 'admin', 'Kate']

for user in users:
    if user == 'admin':
        print(f"\nHello, {user}! You have unlimited rights\n")
    else:
        print(f"Hello, {user}, for your logging")

# Упражнение 5.9 стр. 103
cats = []
if cats:
    for cat in cats:
        print("You are so cute")
else:
    print('We need cats!')

# Упражнение 5.10 стр. 103
current_users = ['Lili', 'Iren', 'Tina', 'Ivan', 'Una', 'Kate']
new_users = ['Sasha', 'iren', 'Rutina', 'Ivan', 'Dasha', 'Tanya']

# преобразуем имена текущих пользователей к нижнему регистру:
low_current_users= [name.lower() for name in current_users]
print(low_current_users)

# преобразуем имена новых пользователей к нижнему регистру:
low_new_users= [name.lower() for name in current_users]
print(low_new_users)

for new_user in new_users:
    if new_user.lower() in low_current_users:
        availability = 'busy'
    else:
        availability = 'available'
    print(f"User {new_user} is {availability}")


# Упражнение 5.11 стр. 104
numbs = list(range(1,10))
print(numbs)

for numb in numbs:
    if numb == 1:
        print('1st')
    elif numb == 2:
        print('2nd')
    elif numb == 3:
        print('3rd')
    else:
        print(f"{numb}th")


