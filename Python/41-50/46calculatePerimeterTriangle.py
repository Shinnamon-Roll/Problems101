def calculatePerimeter(a: float, b: float, c: float) -> float:
    return a + b + c
def main():
    a = int(input("Enter length of ther first side of the triangle : "))
    b = int(input("Enter length of ther first side of the triangle : "))
    c = int(input("Enter length of ther first side of the triangle : "))

    result = calculatePerimeter(a, b, c)
    print(result)
main()