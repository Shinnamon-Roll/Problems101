def containsVowel(s: str) -> bool:
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowelInChar = []
    s = s.lower().replace(' ', '')

    booloon = False  
    for char in s:
        if char in vowel:
            booloon = True
            if char not in vowelInChar:
                vowelInChar.append(char)
    
    print(f"Your words is {s}")
    print(f"Vowels found: {', '.join(vowelInChar)}")
    return booloon

def main():
    while True:
        strings = input("Enter a string to search for vowels (1-100 characters): ")
        count = len(strings)

        if 1 <= count <= 100:
            break
        else:
            print("Please enter a string with 1 to 100 characters.")

    has_vowel = containsVowel(strings)
    print(f"Contains vowel: {has_vowel}")

main()
