def printDiamondPattern(n: int) -> None:
    count = 0
    for _ in range((n * 2) - 1):
        if count < n:
            count += 1
        elif count == n:
            count -= 1
            n -= 1

        print("*" * count)

def main():
    while True:
        number= int(input("Enter the number : "))
        if number < 100 and number > 0:
            break
        else:
            print("Try again...")

    printDiamondPattern(number)

main()