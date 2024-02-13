from operations import *

def calculate(expression):
    num1, operator, num2 = expression.split()
    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        return "Error: Unknown operator."

response = input("enter and equation in the format <num1> <operator> <num2>: ")
print("= ",calculate(response))