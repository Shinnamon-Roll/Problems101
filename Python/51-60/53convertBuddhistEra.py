def convertBeToAd(beYear: int) -> int:
    return beYear - 543

def main():
    beYear = int(input("Enter year: "))
    result = convertBeToAd(beYear)
    print(result)

main()