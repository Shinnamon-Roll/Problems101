def replaceCharacters(s:str):
    s = s.replace('a', '@').replace('l', '1').replace('o', '0')
    return s

def main():
    while True:
        strings = input("Enter a string to search for transform (1-100 characters): ")
        count = len(strings)

        if 1 <= count <= 100:
            break
        else:
            print("Please enter a string with 1 to 100 characters.")

    result = replaceCharacters(strings)
    print(f"Output after replace is : {result}")

main()