def convertThbToCurrency(amount: float, toCurrency: str) -> float:
    myD = {'usd': 0.030, 'eur': 0.027, 'gbp': 0.023, 'jpy':3.4, 'aud':0.045}

    for currency, aamount in myD.items():
        if toCurrency.lower() == currency.lower():
            return amount * aamount

def main():
    print((
    f"{'THB to USD (United States Dollar)':<40}1 THB = 0.030 USD\n"
    f"{'THB to EUR (Euro)':<40}1 THB = 0.027 EUR\n"
    f"{'THB to GBP (British Pound Sterling)':<40}1 THB = 0.023 GBP\n"
    f"{'THB to JPY (Japanese Yen)':<40}1 THB = 3.4 JPY\n"
    f"{'THB to AUD (Australian Dollar)':<40}1 THB = 0.045 AUD"
))
    
    choices = input("What currency do you want to exchange : ")
    money = float(input("How much do you want to exchange (THB): "))

    result = convertThbToCurrency(money, choices)
    print(f"{"Your money in THB is :":<40}{money}\n{"and your money after exchange is :":<40}{result}")

main()
