def find_divisors(number):
    list = []
    for runNum in range(1, number + 1):
        if number % runNum == 0:
            list.append(runNum)
    print(list)

def main():
    number = int(input("Enter a number : "))
    find_divisors(number)

main()