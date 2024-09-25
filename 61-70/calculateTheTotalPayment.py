def calculateTotalPayment(numBills: int, bills: list[float]) -> float:
    total = 0
    myDiscount = {1000: 0.05, 5000: 0.1, 10000: 0.2}
    ddiscount = 0

    for coash in bills:
        total += coash

    for count, discount in reversed(sorted(myDiscount.items())):
        if total > count:
            total = total - (total * discount)
            ddiscount += discount
            break

    return total, ddiscount

def main():
    numBills = int(input("Enter the number of bills : "))
    bills = []

    for count in range(numBills):
        money = int(input(f"Enter {count + 1} bill : "))
        bills.append(money)

    result, discount = calculateTotalPayment(numBills, bills)
    print(f"Your total amount is {result} and your discount is {discount}")
        

main()