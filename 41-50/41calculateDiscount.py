def calculateDiscountedPrices(prices: list[float], discountPercentage: float) -> list[float]:
    result = []

    for price in prices:
        result.append(price * (1 - (discountPercentage / 100)))

    return result

def main():
    prices = [100.0, 250.0, 75.0]
    discount_percentage = 20.0

    result = calculateDiscountedPrices(prices, discount_percentage)
    print(result)

main()