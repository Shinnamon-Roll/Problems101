def primeNumberInRange(start : int, end : int):
    for nums in range(start, end):
    

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

