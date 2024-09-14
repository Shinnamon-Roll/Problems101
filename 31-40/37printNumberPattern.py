def printNumberPattern(rows: int) -> None:
     for i in range(1, rows + 1):
        print('-' * (rows - i), end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print()

def main():
    rows = int(input("Enter a number for rows : "))

    printNumberPattern(rows)

main()