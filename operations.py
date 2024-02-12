def divide(num, den):
    if den == 0:
        print("Error! Division by zero is not allowed.")
        return None
    return num / den

def add(a, b) : 
    return a+b

def subtract(a, b):
    return a - b

def multiply(a, b) :
    result = 0
    if b < 0 : b = b * -1
    for _ in range(b):
        result = add(result, a)
        
    return result