def primeNumberInRange(start : int, end : int):
    primeToCal = 0
    totalPrime = []
    for nums in range(start, end + 1):
        primeNum = []
        for i in range(1, nums + 1):
            if nums % i == 0:
                primeNum.append(i)
        if primeNum[0] == 1 and primeNum[1] == nums:
            totalPrime.append(nums)
            primeToCal += nums
    print("Total prime numbers are :", totalPrime,"and", primeToCal ,"is sum of prime numbers")

def main():
    
    while True:
        start = int(input("Enter a start number : "))
        end = int(input("Enter a end number : "))

        if start > 1 and start < 1000 and start < end and end < 1000:
            break
        else:
            print("Error : Invalid number")
            pass

    primeNumberInRange(start, end) 


main()

