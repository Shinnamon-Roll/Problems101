def groupByUnitDigit(numbers: list[int]) -> list[list[int]]:
    count = 0
    result = []
    while count < 10:
        listTemp = []
        for num in numbers:
            if num % 10 == count:
                listTemp.append(num)
        result.append(listTemp)
        count += 1
     
    return result
    
def main():
    numbers = [21, 34, 51, 23, 37, 44, 60, 11, 91, 99]

    result = groupByUnitDigit(numbers)
    print(result)

main()