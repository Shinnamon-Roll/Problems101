def separateEvenOdd(numbers: list[int]) -> tuple[list[int], list[int]]:
    evenList = []
    oddList = []

    for num in numbers:
        if num % 2 == 0:
            evenList.append(num)
        else:
            oddList.append(num)

    resutl = tuple([evenList] + [oddList])

    return resutl

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = separateEvenOdd(numbers)
    print(result)

main()