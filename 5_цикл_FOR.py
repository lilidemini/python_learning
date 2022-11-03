languages = ["rus", "en", "chi", "deu", "fra"]

for language in languages:
    print(language.upper())
    print(f"I know {language} language\n")

# rus
# I know rus language
#
# en
# I know en language
#
# chi
# I know chi language
#
# deu
# I know deu language
#
# fra
# I know fra language


for language in languages:
    print(language.upper())
print("I know " + language + ' language\n')

# RUS
# EN
# CHI
# DEU
# FRA
# I know fra language


# Упражнение 4.1 страница 71
pizzas = ["Pepperini", '4 cheeze', '4 seasons', 'DoDo']
for i in pizzas:
    print('I like to eat '+ i)
print("I really like pizza")
