# Создадим модуль pizza в одном каталоге с файлом 15.2_импорт_функций.py
# Модуль - файл с расширением .py, содержащий код, который нужно импортировать.


# ИМПОРТИРОВАНИЕ ВСЕХ ФУНКЦИЙ В МОДУЛЕ: import имя_модуля

# Импортируем в программу модуль pizza со всеми функциями
import pizza

# Вызовем дважды функцию make_pizza
pizza.make_pizza(16, 'pepperoni') # We can make 16sm pizzas: pepperoni
pizza.make_pizza(20, 'margarita', 'cheese') # We can make 20sm pizzas: margarita cheese


# ИМПОРТИРОВАНИЕ КОНКРЕТНОЙ ФУНКЦИИ: from имя_модуля import имя_функции
# при импорте нескольких функций: from имя_модуля import функция_0, функция_1

# импортируем функцию make_pizza
from pizza import make_pizza

# Вызовем дважды функцию make_pizza
make_pizza(16, 'pepperoni') # We can make 16sm pizzas: pepperoni
make_pizza(20, 'margarita', 'cheese') # We can make 20sm pizzas: margarita cheese
# при импорте конкретной функции не обязательно использовать точечную запись,
# так как мы явно импортировали функцию from pizza import make_pizza

# ПСЕВДОНИМ ДЛЯ ФУНКЦИИ (alias): from имя_модуля import имя_функции as псевдоним
from pizza import make_pizza as mp

# ПСЕВДОНИМ ДЛЯ МОДУЛЯ: import имя_модуля as псевдоним
import pizza as p

# ИМПОРТИРОВАНИЕ ВСЕХ ФУНКЦИЙ МОДУЛЯ: from имя_модуля import *