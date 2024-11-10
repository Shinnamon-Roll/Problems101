def reverseString(s:str):
    characters = list(s)
    characters.reverse()
    
    return ''.join(characters)

def main():
    while True:
        strings = input("Enter a string : ")
        count = len(strings)

        if 1 <= count <= 100:
            break
        else:
            print("Please enter a string with 1 to 100 characters.")

    result = reverseString(strings)
    print(f"Output is : {result}")

main()