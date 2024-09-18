def calculateAnnualReturn(initialInvestment: float, finalInvestment: float, years: int) -> float:
    print(f"Resulte is : {((finalInvestment / initialInvestment) ** (1 / years)) - 1:.2f}")

def main():
    initialInversment = int(input("Enter a initial inversment : "))
    finalInversment = int(input("Enter a final inversment : "))
    years = int(input("Enter a years : "))

    calculateAnnualReturn(initialInversment, finalInversment, years) 

main()