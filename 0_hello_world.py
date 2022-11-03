# 1. ПЕРЕМЕННЫЕ
print('Hello, world')

# Присвоим в переменную "message" значение "Hello, world"
message = 'Hello, world'
print(message)

# Изменим значение первоначальной переменной message
message = "Goodbye world"
print(message) #  Goodbye world

# 2. СТРОКИ - простая последовательность символов
'This is a string'
"This is also a string"

# Строки мб заключены в апострафы и в двойные кавычки.
# При необходимости можно использовать одновременно и апостроф и кавычки:
'I told my friend: "Python is my favourite language"'

# Изменение регистра сиволов в строках
# метод title() преобразует 1-й символ КАЖДОГО слова в строке к верхнему регистру
name = "lili demini"
print(name.title()) # Lili Demini

# методы upper() и lower() преобразует ВСЕ символы каждого слова в строке к верхнему и нижнему регистру соответсвенно
name = "LiLi DeMini"
print(name.upper()) #LILI DEMINI
print(name.lower()) #lili demini

# Переменные внутри строки: f-строки
first_name = 'LILIA'
last_name = 'yagyaeva'
print(f"{first_name} {last_name}") #LILIA yagyaeva

full_name = f"{first_name.lower()} {last_name.lower()}"
print(full_name) #lilia yagyaeva

print(f'Hello, {full_name.title()}') #Hello, Lilia Yagyaeva
message = f'Hi, dear {full_name.title()}' #Hi, dear Lilia Yagyaeva
print(message)

# Табуляция (отступ): \t
print('Python') #Python
print('\tPython') # Python

# Разрыв строк (новый абзац): \n
print('Languages:\nPython\nC\nJavaScript')
# Languages:
# Python,
# C,
# JavaScript

# Сочетание табуляции + разрывы строк: \n\t
print('Languages:\n\tPython\n\tC\n\tJavaScript')
# Languages:
# 	Python
# 	C
# 	JavaScript


# Удаление пробелов .strip(), .rstrip(), .lstrip()
language = 'python '
print(language.rstrip()) #удалит пробел справа, но не изменит значение в переменной, так и останется с пробелом
print(language) #значение в переменной с пробелом справа

language=language.rstrip() #удалит пробел справа в значении переменной навсегда
print(language) #значение в переменной без пробела

#Упражнение 2.3 стр.42
user_name = 'yasmin'
user_greeting_message = f"Hello, {user_name.title()}, would you like to learn some Python today"
print(user_greeting_message)

#Упражнение 2.4 стр.43
print(user_name.lower(), user_name.upper(), user_name.title())

#Упражнение 2.4 стр.43
quote_author=' albert einstein '
quote=' a person who never made a mistake never tried anything new.'
print(f'\t{quote_author.strip().title()} once said,\n\t"{quote.title().strip()}"')

# 3. ЧИСЛА
# Целые числа
print(2+3) # сложение
print(3-2) # вычитание
print(2*3) #произведение
print(3/2) #деление
print(3**2) #возведение во 2 степень
print((2 + 3) * 2) #несколько операций

# Вещественные числа - числа, имеющие дробную часть
print(6/2) # 3.0, при делении всегда в ответе вещественное число
print(2+3.0) # 5.0, в любых операциях при смешении целого и вещественного числа в ответе вещественное число

# Символы подчеркивания в числах для удобства чтения целых и вещественных чисел
print(1_000, 100_0, 1000) #1000 1000 1000

# Множественное присваивание - чаще используется с числами
a, b, c = 1, 2, 3
print(a,b,c) #1 2 3

# Константа - неизменная переменная, задается буквами верхнего регистра
MAX_CONNECTIONS=5000

#Упражнение 2.8 стр.46
my_favorite_number = 8
print(f'My favourite number is {my_favorite_number}')

# The Zen of Python или Дзен Питона
import this

# 4. СПИСКИ
