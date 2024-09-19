def calculateRectangleArea(width: float, length: float) -> float:
    return width * length

def main():
    width = int(input("Enter width: "))
    length = int(input("Enter length: "))
    result = calculateRectangleArea(width, length)

    print(result)

main()
