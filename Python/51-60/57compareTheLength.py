def compareStringLengths(str1: str, str2: str) -> str:
    if len(str1) > len(str2):
        return f"{str1} is longer then {str2} : {len(str1) - len(str2)} characters"
    
    elif len(str1) < len(str2):
        return f"{str1} is shorter then {str2} : {len(str2) - len(str1)} characters"

def main():
    str1, str2 = input("Enter two string to compare : ").split(" ")
    result = compareStringLengths(str1, str2)
    print(result)

main()