# функция range() выводить числовые последовательности
for value in range(1,5): # последняя цифра не выведется
     print(value)

# 1
# 2
# 3
# 4

for value in range(5): # если передана одна цифра, то отсчет начинается с 0
     print(value)

# 0
# 1
# 2
# 3
# 4

# Создание числовых списков
numbers = list(range(5))
print(numbers) # [0, 1, 2, 3, 4]

# Построение списка четных числел
even_numbers = list(range(2,11,2))
print(even_numbers) # [2, 4, 6, 8, 10]

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# или

squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Простая статистика с числовыми списками
digits = []
for i in range(9):
    digits.append(i)
print(digits) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(min(digits)) # 0
print(max(digits)) # 8
print(sum(digits)) # 36
print(len(digits)) # 9

# ГЕНЕРАТОР СПИСКОВ
squares = [value**2 for value in range(1,4)]
print(squares) # [1, 4, 9]

# Упражнение 4.3 стр 75
twenty = [i for i in range (1, 21)]
print(twenty) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

odd_numbers = []
for i in range(1,21,2):
    odd_numbers.append(i)
print(odd_numbers) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

cube = [i**3 for i in range(1,11)]
print(cube) # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
