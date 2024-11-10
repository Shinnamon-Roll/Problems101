def printDiamondPattern(n: int) -> None:
    count = 0
    check = 1
    for _ in range(n - 1):
        multiply = n / 2
        multiply = int(multiply)

        print("*" * multiply + "_" * count + "*" * multiply)

        if multiply > check :
            count += 2
            n -= 2
        else:
            check += 1
            count -= 2
            n += 2

def main():
    while True:
        number = int(input("Enter a number : "))

        if number < 100 and number > 0:
            if number % 2 == 0:
                break
            else:
                print("Pleas enter odd number...")
        else:
            print("Pleas enter 2 - 100 number...")

    printDiamondPattern(number)

main()