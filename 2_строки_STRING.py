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
