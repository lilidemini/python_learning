# BREAKE - команда для выхода из цикла
prompt = "\nWhat is your favourite city"
prompt += "\n(Enter 'quit' to finish)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I`d love to go to {city}")