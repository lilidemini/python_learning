# импортирование одного класса из модуля
from electric_car import ElectricCar as EC

# импортирование нескольких классов из модуля
from electric_car import ElectricCar, Battery

# импортирование всего модуля
import cars

# импортирование модуля в модуль смотри в модуле electric_car

# СТАНДАРТНЫЕ БИБИЛИОТЕКИ Python:
# 1. модуль random с функциями randit, choice
from random import randint, choice, choices

print(randint(1,6)) # случайное целое число в диапазоне от 1 до 6

players = ['lili', 'kate', 'irina']
print(choice(players)) # возвращает случайный элемент из списка или кортежа

# упражнение 9.13 стр 194
class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

def model_roll(die, n=10):
    print(f'Кубик {die.sides} граней')
    for i in range(n):
        print(die.roll_die())

model_roll(Die(20))

# упражнение 9.14 стр 194

list = [1, 3, 4, 4, 5, 6, 9, 7, 4, 0, "A", "O", "P", "S", "Q"]

lucky_ticket = []
for i in range(4):
    lucky_ticket.append(choice(list))
    print(lucky_ticket)

# упражнение 9.15 стр 194
lottery = [1, "S"]
my_ticket = ['S', 1, 1, 'S']

count = 0
while True:
    winner = choices(lottery, k=4)
    count += 1

    if winner == my_ticket:
        break

print(count)


