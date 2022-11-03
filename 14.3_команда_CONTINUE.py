# CONTINUE - команда для возвращения к началу цикла и проверке условия

# пример: цикл, который считает от 1 до 10 и выводит только нечетные числа:
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    else:
        print(i)

# Упражнение 7.4 стр 138

add = "Add ingredients to your pizza or quit to finish: "

while True:
    pizza = input(add)

    if pizza == 'quit':
        break
    else:
        print(f"{pizza} was added")

# Упражнение 7.5 стр 138
check = 'Enter your age: '


while True:
    age = int(input(check))

    if age < 3:
        price = 'free'
    elif (age >= 3) and (age <= 12):
        price = '10$'
    else:
        price = '15$'
    print(f"The cost of ticket is {price}")


