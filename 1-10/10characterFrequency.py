def characterFrequency(strings: str): 
    empList = []
    
    for chars in strings:
        for char in chars:
            charCount = 0
            if not char in empList:
                empList.append(char)
                charCount += 1
                print(charCount)
            if charCount == empList:
                charCount += 1
                print(charCount)


    print(empList)


def main():
    strings = list(map(str, input("Enter multiple values: ").split()))
    characterFrequency(strings)

main()

# hello world test case example