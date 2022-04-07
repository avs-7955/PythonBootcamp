import art
import os
def clear(): os.system('cls')

# Addition


def add(num_01, num_02):
    '''Function takes two paramers as input and returns the sum.'''
    return (num_01 + num_02)


# Subtraction
def subtract(num_01, num_02):
    '''Function takes two paramers as input and returns the difference.'''
    return (num_01 - num_02)


# Multiplication
def multiply(num_01, num_02):
    '''Function takes two paramers as input and returns the product.'''
    return (num_01 * num_02)


# Division
def divide(num_01, num_02):
    '''Function takes two paramers as input and returns the quotient.'''
    return (num_01 / num_02)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


flag = ''
while(1):
    print(art.logo)
    if(flag == 'y'):
        num01 = result
    else:
        clear()
        print(art.logo)
        num01 = float(input("What is your first number?\n"))

    for operation in operations:
        print(operation)
    operation_symbol = input("Pick an operation from the line above: ")
    calculation_result = operations[operation_symbol]
    num02 = float(input("What is your second number?\n"))
    result = calculation_result(num01, num02)

    print(f"{num01} {operation_symbol} {num02} = {result}")
    flag = input(
        f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculator: ")
