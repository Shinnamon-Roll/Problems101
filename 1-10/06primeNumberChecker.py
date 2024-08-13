def checkPrime(numbers):
    divided = []

    for num in range(1, numbers + 1):
        if numbers % num == 0:
            divided.append(num)
    
    if divided[0] == 1 and divided[1] == numbers :
        print("Prime numbers")

    else:
        print("not prime numbers")

def main():
    while True:
        number = int(input("\nEnter a number : "))
        if number > 1 and number <= 10000:
            break
        elif number == 1:
            print("It's not prime...Please try again.")
            pass
        else:
            print("Input number incorrect...Please try again.") 
            pass
    checkPrime(number)
    
main()