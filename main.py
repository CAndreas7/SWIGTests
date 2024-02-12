def add(a, b) : 
    return a+b

def multiply(a, b) :
    result = 0
    if b < 0 : b = b * -1
    for _ in range(b):
        result = add(result, a)
        
    return result