def findDivisors(num: int) -> list:
    result = []
    for number in range(1, num + 1):
        if num % number == 0:
            result.append(number)

    return result

def main():
    number = int(input("Enter a number to find the divisors : "))

    result = findDivisors(number)
    print(result)
main()