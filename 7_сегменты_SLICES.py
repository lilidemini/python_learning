# Сегменты (slices) - отдельные элементы списка


list = ["Carl", "megan", "Iren", "Ameli"]

print(list[1:3]) #['megan', 'Iren']

print(list[:3]) # ['Carl', 'megan', 'Iren']

print(list[1:]) #['megan', 'Iren', 'Ameli']

# вывод последние два  элемента списка
print(list[-2:]) # [ 'Iren', 'Ameli']

print(list[:-2]) # ['Carl', 'megan']

for i in list[:2]:
    print(i)
# Carl
# megan

# Копирование списка
list = ["Carl", "megan", "Iren", "Ameli"]
copy_list = list[:]
copy_list.append("Oleg")
print(list) # ['Carl', 'megan', 'Iren', 'Ameli']
print(copy_list) # ['Carl', 'megan', 'Iren', 'Ameli', 'Oleg']

# Упражнение 4.10 стр 79

print(f'\nFirst three items are: {list[:3]}') # First three items are: ['Carl', 'megan', 'Iren']
print(f'\nTwo items from the middle are: {list[1:3]}') # Two items from the middle are: ['megan', 'Iren']
print(f'\nLast three items are: {list[-3:]}') # Last three items are: ['megan', 'Iren', 'Ameli']
