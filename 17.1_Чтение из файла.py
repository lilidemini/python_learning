# open - функция, возвращает объект, представляющий файл

# открыть и вывести содержимое файла 'pi_digits.txt'
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# конструкция с ключевым словом with закрывает файл, если он больше не используется.
# read - метод, читает содержимое файла
# rstrip() - метод, удаляет все пропуски в конце строки

# ЧТЕНИЕ СТРОК В ФАЙЛЕ
# для доп обработки каждой строки файла используем цикл FOR
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# СОЗДАНИЕ СПИСКА СТРОК из данных файла
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())

# построим одну строку из данных файла
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string) # 3.141592653589793238462643383279
print(len(pi_string)) # 32


