def calculateCoins(amount: int) -> tuple[int, int, int, int]:
    tenCoin = 0
    fiveCoin = 0
    twoCoin = 0
    oneCoin = 0

    while True:
        if amount >= 10:
            tenCoin = amount // 10
            amount = amount - (tenCoin * 10)
        elif amount >= 5:
            fiveCoin = amount // 5
            amount = amount - (fiveCoin * 5)
        elif amount >= 2:
            twoCoin = amount // 2
            amount = amount - (twoCoin * 2)
        else:
            oneCoin = amount  
            break

    result = (tenCoin, fiveCoin, twoCoin, oneCoin)
    return result

def main():
    while True:
        try:
            amount = int(input("Enter your money to exchange to coin (0 for done): "))

            if amount == 0:
                break 

            if not isinstance(amount, (int)):
                print("your money is not Integer...")
            else:
                result = calculateCoins(amount)
                print(result)

        except ValueError:
            print("Yes mae mung")
main()