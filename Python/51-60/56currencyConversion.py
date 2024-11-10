def convertCurrency(amount: float, fromCurrency: str, toCurrency: str) -> float:
    myD = {'usd':1, 'eur': 0.85, 'gbp': 0.75, 'jpy': 110.0, 'thb': 32.0}

    for currency, money in myD.items():
        if fromCurrency.lower() == currency:
            amount /= money
            for i, j in myD.items():
                if toCurrency.lower() == i:
                    return f"{amount * j:.2f}"

def main():
    print("Supported Currencies\nUSD (United States Dollar)\nEUR (Euro)\nGBP (British Pound Sterling)\nJPY (Japanese Yen)\nTHB (Thai Baht)")
    amount, fromCurrency, toCurrency = input("Enter _Amount_ _currentCurrency_ _toCurrency_ : ").split(" ")
    amount = float(amount)

    result = convertCurrency(amount, fromCurrency, toCurrency)
    print(result)
main()