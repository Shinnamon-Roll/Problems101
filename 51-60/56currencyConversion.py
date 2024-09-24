def convertCurrency(amount: float, fromCurrency: str, toCurrency: str) -> float:
    myD = {'eur': 0.85, 'gbp': 0.75, 'jpy': 110.0, 'thb': 32.0}



def main():
    print("Supported Currencies\nUSD (United States Dollar)\nEUR (Euro)\nGBP (British Pound Sterling)\nJPY (Japanese Yen)\nTHB (Thai Baht)")
    amount, fromCurrency, toCurrency = input("Enter _Amount_ _currentCurrency_ _toCurrency_ : ").split(" ")
    amount = float(amount)

    result = convertCurrency(amount, fromCurrency, toCurrency)
    print(result)
main()