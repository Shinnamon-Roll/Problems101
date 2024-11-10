def calculateStatistics(t: tuple[int, ...]) -> tuple[tuple[int, ...], int, int, int, float]:
    squaredValueslist = []
    Summernumber = 0
    for i in t:
        cal = i ** 2
        squaredValueslist.append(cal)

    maxValue = max(squaredValueslist)
    minValue = min(squaredValueslist)
    for j in squaredValueslist:
        Summernumber += j 

    averag_num = Summernumber/len(t)
    squaredValues = tuple(squaredValueslist)

    print(f"\nsquared values is : {squaredValues}\nmax value is : {maxValue}\nmin value is : {minValue}\nAverage value is : {averag_num}")
        

def main():
    number = (1,2,3,4,5,6,7,8,9,10)
    calculateStatistics(number)
    # print(results)

main()
