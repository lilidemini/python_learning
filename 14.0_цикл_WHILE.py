# цикл FOR получает элементы и выполняет код по одному разу для каждого элемента
# цикл WHILE продолжает выполняться, пока остается истинным некоторое условие

current_number = 1
while current_number < 5:
    print(current_number) # 1 2 3 4 цикл повторяется, пока выполняется условие while
    current_number += 1
    # оператор += является сокращенной формой записи current_number = current_number + 1

# прерывание работы цикла
prompt = "\nEnter 'quit' to end the program."
prompt += "\nTell me smth and I will repeat it back to you: "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

