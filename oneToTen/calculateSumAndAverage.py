def calculateSumAndAverage(number):
    
    result = 0
    for num in number:
        calculate = num + result
        result += calculate

    average = result / len(number) 

    print("Total is :", result)
    print("Average is :", average)
    
def main():

    numSets = []
    count = 1

    while True:
        number = float(input("Enter the number :" ))

        numSets.append(number)
        count += 1
    
        if count == 6:
            break
    
    calculateSumAndAverage(numSets)
    
main()
