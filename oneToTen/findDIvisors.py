def find_divisors(number):
    list = []
    for runNum in range(1, number + 1):
        if number % runNum == 0:
            list.append(runNum)
    print(list)

def main():
    while True:
        number = int(input("\nEnter a number : "))
        if number > 0 and number <= 1000:
            break
        else:
            print("Input number incorrect...Please try again.") 
            pass
    find_divisors(number)

main()