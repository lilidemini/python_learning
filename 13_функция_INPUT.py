# INPUT - функция для получения данных в строковом формате

name = input(f'What`s your name: ')
print(f"Hello, {name}")

message = 'Tell us who you are'

# += добавляет значение в уже существующую переменную
message += f"\nMy name is {name}"
print(message)


# int - функция для преобразования строки в число
age = int(input(f"How old are you? "))
print(age > 18) # True

# Упражнение 7.1
car = input(f"Which car do you want to rent?")
print(f"Let me see if I can find you a {car.title()}")

# Упражнение 7.2
guests = int(input(f"How many guests do you want to reserve a table? "))
if guests > 8:
    print("Please, wait")
else:
    print('Table was reserved')