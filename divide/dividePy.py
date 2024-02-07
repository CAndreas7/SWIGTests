def dividePy(num, den):
    if den == 0:
        print("Error! Division by zero is not allowed.")
        return None
    return num / den

num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))
result = dividePy(num, den)

if result is not None:
    print(f"The result is: {result}")
