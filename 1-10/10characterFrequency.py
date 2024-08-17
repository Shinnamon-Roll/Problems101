def characterFrequency(*args: str) -> dict:
    combined_string = ''.join(args)

    frequencyDict = {}

    for char in combined_string:
        if char in frequencyDict:
            frequencyDict[char] += 1
        else:
            frequencyDict[char] = 1
    
    return frequencyDict

def main():
    strings = []
    for i in range(5):
        strings.append(input(f"Enter string {i+1}: "))
    
    result = characterFrequency(*strings)
    
    print(result)

main()
