import random

letters = ['a''b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

symbols = ['!', '*', '#', '%', '^', '&', '>', '<', '+', '-']

print('Welcome to the Py Password Generator')

input_letters = input('How many letters would you like in your password? => ')
input_symbols = input('How many symbols would you like? => ')
input_numbers = input('How many numbers would you like? => ')

if not input_letters.isdigit() or not input_symbols.isdigit() or not input_numbers.isdigit():
    print('Invalid input. Please enter a number!')
else:
    password = []

    random_letters = random.randint(0, 50)
    for i in range(0, int(input_letters)):
        random_letters = random.randint(0,51)
        password.append(letters[random_letters])

    random_numbers = random.randint(0,9)
    for i in range(0, int(input_letters)):
        random_numbers = random.randint(0,9)
        password.append(numbers[random_numbers])

    random_symbols = random.randint(0,10)
    for i in range(0, int(input_symbols)):
        random_symbols = random.randint(0,8)
        password.append(symbols[random_symbols])

    random.shuffle(password)
    print(f"Here is your password: {''.join(password)}")
    
    if len(password) <= 7:
        print('Your password is weak, try to increase the length of your password.')
    else:
        print('Your password is strong.')