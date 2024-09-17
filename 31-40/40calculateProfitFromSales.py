def calculateProfit(sales: tuple[float, float, float, float, float], costs: tuple[float, float, float, float,float]) -> tuple[tuple[float, float, float, float, float], float]:
    result = []
    count = 1

    for sale in sales:
        print(sale)
        print(costs)
        count += 1

    return result

def main():
    sales = (10000.0, 15000.0, 20000.0, 25000.0, 30000.0)
    costs = (7000.0, 8000.0, 9000.0, 11000.0, 12000.0)

    result = calculateProfit(sales, costs)
    print(result)


main()