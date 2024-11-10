def calculateMedian(provinces: dict[str, int]) -> list[tuple[str, int]]:
    median = []
    result = {}
    
    for value in provinces.values():
        median.append(value)

    median = removeHeadTail(sorted(median))

    for key, value in provinces.items():
        if value == median:
            result[key] = value

    return result

def removeHeadTail(median):
    while True:
        del median[0]
        del median[-1]

        if len(median) == 1 or len(median) == 2:
            break
    median = median[0]
    return median

def main():
    data = {}
    for _ in range(5):
        inputKey, inputValue = input("Enter your country and number (0 for done) : ").split()
        inputValue = int(inputValue)

        if inputValue > 0 and inputValue < 100:
            data[inputKey] = inputValue
            print(f"--- {data} ---")
        else:
            pass

    result = calculateMedian(data)
    print(result)

main()