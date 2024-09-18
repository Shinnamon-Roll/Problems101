def calculateInvestmentGrowth(principal: float, annualRate: float, years: int) -> list[float]:
    for n in range(1, years + 1):
        print(f"For the {n} year : {principal * ((1 + (annualRate / 100)) ** n):.2f}")

def main():
    principal = int(input("\nEnter principal : "))
    annualRate = int(input("Enter annual rate : "))
    years = int(input("Enter years : "))

    calculateInvestmentGrowth(principal,annualRate, years)


main()