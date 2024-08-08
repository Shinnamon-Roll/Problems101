def findNonMultiplesOfThreeFourAndFive(start:int,end:int):
    result = []

    for number in range(start, end):
        if not number % 3 == 0 and not number % 4 == 0 and not number % 5 == 0:
            result.append(number)
        else:
            pass

    print("\nYou are input number :", start , "and", end)
    print(result)

def main():
    while True:
        numStart = int(input("Input your start number : "))
        numEnd = int(input("Input your end number : "))
        if numStart > 1 and numStart < 1000 and numStart < numEnd and numEnd > 1 and numEnd < 1000 and numEnd > numStart:
            break
        else:
            print("Please enter again --- ")
            pass

    findNonMultiplesOfThreeFourAndFive(numStart,numEnd)

main()
