def printRectanglePattern(rows: int, columns: int) -> None:
    for row in range(rows):
        print("*" * columns)

def main():
    while True:
        rows = int(input("Enter a rows : "))
        columns = int(input("Enter a column : "))

        if rows > 100 or rows < 0 or columns > 100 or columns < 0:
            print("try again...")
        else:
            break

    printRectanglePattern(rows, columns)

main()