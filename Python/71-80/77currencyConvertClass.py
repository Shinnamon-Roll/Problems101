class CurrencyConverter:
    def __init__(self, Amount: float, Currency: str):
        self.Amount = Amount
        self.Currency = Currency

    def ConvertTo(self, TargetCurrency: str) -> float:
        conversionRates = {
            'USD': {
                'EUR': 0.85,
                'GBP': 0.75,
                'JPY': 110,
                'THB': 32,
            },
            'EUR': {
                'USD': 1.18,
                'GBP': 0.88,
                'JPY': 129.86,
                'THB': 37.64,
            },
            'GBP': {
                'USD': 1.33,
                'EUR': 1.14,
                'JPY': 147.69,
                'THB': 42.73,
            },
            'JPY': {
                'USD': 0.0091,
                'EUR': 0.0077,
                'GBP': 0.0068,
                'THB': 0.29,
            },
            'THB': {
                'USD': 0.031,
                'EUR': 0.026,
                'GBP': 0.023,
                'JPY': 3.47,
            }
        }

        if self.Currency not in conversionRates or TargetCurrency not in conversionRates[self.Currency]:
            raise ValueError("Invalid currency code")

        ConvertedAmount = self.Amount * conversionRates[self.Currency][TargetCurrency]
        return round(ConvertedAmount, 2)

# Example usage
def main():
    Amount = float(input("Enter the amount: "))
    Currency = input("Enter the currency (USD, EUR, GBP, JPY, THB): ").upper()
    TargetCurrency = input("Enter the target currency (USD, EUR, GBP, JPY, THB): ").upper()

    Converter = CurrencyConverter(Amount, Currency)
    ConvertedAmount = Converter.ConvertTo(TargetCurrency)

    print(f"{Amount} {Currency} is equal to {ConvertedAmount} {TargetCurrency}")

if __name__ == "__main__":
    main()
