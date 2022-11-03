cars = ["audi", "bmw", "kia", "subary"]

for car in cars:
    if car == "bmw": # проверяет содержит ли car значение "bmw"
        print(car.upper()) # если проверка положительная, то значение выводится в верхнем регистре
    else:
        print(car.title()) # если проверка отрицательно, то значение выводится с заглавной буквы
# Audi
# BMW
# Kia
# Subary

# Проверка равенства с учетом регистра ==
car = "Audi" #одинарное = выполняет операцию присвоения
car == "audi" #False
car.lower() == "audi" #True

# Проверка НЕравенства !=
car = "bmw"
if car != "audi": # проверка что значение car не равно audi
    print("I wanna just Audi and ahythig else") # I wanna just Audi and ahythig else

# Сравнение чисел
age = 19

if age<=18:
    print("You are young")
else:
    print("You are adult") # You are adult

# Проверка нескольких условий: AND - истина, если оба условия выполняются
age_0 = 28
age_1 = 30
age_0 >= 29 and age_1 >=29 # False
# для читабельности кода лучше отдельные условия в скобках
(age_0 >= 27) and (age_1 >=27) # True

# Проверка нескольких условий: OR - истина, если хотя бы одно условие выполняется
(age_0 >= 29) or (age_1 >=29) # True
(age_0 >= 31) or (age_1 >=31) # False

# Проверка вхождения значений в список: IN
family = ['father', 'mother', 'children', 'grandmother', 'grandfather']
'father' in family # True
'Father' in family # False
"father" in family # True

# Проверка отсутвия значений в списке: NOT IN
users = ["Una", "Irina", "Anna"]
"Liliya" not in users # True
"Una" not in users # False
"una" not in users # True

user = "Yasmin"
if user not in users:
    print(f"{user.title()}, sorry, you are not registered")

# Упражнение 5.1 стр.93
print(f'\nFirst condition:')
me = 'mother'

print("\nIf I am == 'mother', it will be True")
print(me == 'mother')

print("\nIf I am  == 'daughter', it will be False")
print(me == 'daughter')

print(f'\nSecond condition:')
my_car = "KIA"

print(f"\nIt is TRUE, that my car == kia")
print(my_car.lower() == "kia")

print(f"\nIt`s FALSE, that my car == audi")
print(my_car == 'audi')

print(f"\nThird condition:")
my_name = "Lili"

print(f"\nIt`s TRUE, that my name is not Anna")
print(my_name != "Anna")

print(f"\nIt`s FALSE, that my name is not Lili")
print(my_name != "Lili")

my_age = 28
daughter_age = 7
husband_age = 30

print(f"\nIt`s FALSE that each member is adult in family")
print((my_age >= 18) and (daughter_age >= 18) and (husband_age >= 18))

print(f'\nIt`s TRUE that we have a children in family')
print((my_age<=18) or (daughter_age<=18) or (husband_age)<=18)

family = ['father', 'mother', 'children', 'grandmother', 'grandfather']
member = 'sister'

if member not in family:
    print(f"Sorry, {member.lower()}, yor are not in family")
else:
    print(f"{member} is member of our family")

print("father" in family) # True
print('father' not in family) # False


