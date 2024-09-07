import os
from art import logo

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

operators = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

def calculator():
    print(logo)

    first_number = float(input('What is the first number? '))
    for operator in operators:
        print(operator)
        run = True
    
    while run:
        input_operator = input("Enter a math operator: ")
        second_number = float(input("What's the next number? "))
        calculation = operators[input_operator]
        answer = calculation(first_number, second_number)
        print(f"{first_number} {input_operator} {second_number} = {answer}")


        if input(f"Type 'y' to continue calculation with the answer or type 'n' to start a new calculation: ") == 'y':
            first_number = answer
        else:
            run = False
            os.system('cls')
            calculator()

calculator()
