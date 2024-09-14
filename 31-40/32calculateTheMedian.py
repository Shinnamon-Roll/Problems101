def calculateMedian(list: list[int]) -> float:
    while True:
        del list[0]
        del list[-1]

        if len(list) == 1 or len(list) == 2:
            break
            
    return list
    
def main():
    numList = []
    while True:
        inputNubmer = int(input("Enter the number(0 for end) "))
        if inputNubmer == 0:
            break

        if inputNubmer < 0 or inputNubmer >= 1000:
            pass
        else:
            numList.append(inputNubmer)
    print(numList)

    result = calculateMedian(sorted(numList))

    print(result)


main()