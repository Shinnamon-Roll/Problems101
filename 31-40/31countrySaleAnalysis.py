def highestSalesCountry(sales: dict[str, int]) -> tuple[str, int]:
    temp = {}
    check = 0
    for key, values in sales.items():
        if values > check:
            temp = {}
            temp[key] = values
            check = values

    return temp

def main():
    salesData = {}
    for _ in range(5):
        inputKey, inputValue = input("Enter your Country and sales : ").split()
        salesData[inputKey] = int(inputValue)
        print(salesData)

    result = highestSalesCountry(salesData)
    print(result)

main()