def averageLengthOfString(strings:list[str]) -> float:
    charCount = 0
    length = []
    for char in strings:
        charCount += len(char)
        length.append(len(char))
    if charCount > 100:
        print(f"Invalid string please input lower than 100 characters({charCount})")
        main()

    calculateChar = charCount / len(strings)
    print(f'Length of string is {length}\nAverage length is {calculateChar}')

def main():
    strings = list(map(str, input("Enter multiple values: ").split()))
    averageLengthOfString(strings)

main()