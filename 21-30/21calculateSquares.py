def calculateStatistics(t: tuple[int, ...]) -> tuple[tuple[int, ...], int, int, int, float]:
    squaredValues = ()
    for i in t:
        cal = i * t
        print(cal)

def main():
    number = (1,2,3,4,5,6,7,8,9,10)
    results = calculateStatistics(number)
    print(results)

main()
