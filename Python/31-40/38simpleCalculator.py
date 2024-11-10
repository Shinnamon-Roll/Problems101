def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:    
    return a / b

def main():
    while True:
        a, operator, b = input("Enter number to calculate (1 + 2) : ").split()
        a = int(a)
        b = int(b)

        if operator == "+":
            result = add(a, b)
            print(result)
        elif operator == "-":
            result = subtract(a, b)
            print(result)
        elif operator == "*":
            result = multiply(a, b)
            print(result)
        elif operator == "/":
            result = divide(a, b)
            print(result)
        else:
            print("kuy")

main()