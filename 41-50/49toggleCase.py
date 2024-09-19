def toggleCase(s: str) -> str:
    keephee = ''
    for char in s:
        if char.isalpha():
            if char == char.upper():
                keephee = keephee + char.lower()
            elif char == char.lower():
                keephee = keephee + char.upper()
        else:
            keephee = keephee + char
            
    return keephee

def main():
    word = input("Enter word to convert : ")

    result = toggleCase(word)
    print(result)

main()