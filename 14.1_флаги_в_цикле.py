# Переменная-флаг сообщает должна ли программа выполняться далее: True или False
# Флаг можно называть как угодно

# пример с флагом active

active = True
while active:
    message = input('Hey, input smth: ')

    if message == 'quit':
        active = False
    else:
        print(message)

