def cumulativeSum(n: int) -> int:
    return f"The result is :{(n * (n + 1)) / 2:.0f}"

def main():
    n = int(input("Enter number : "))

    result = cumulativeSum(n)
    print(result)

main()