def checkMembership(s: set, value: str) -> bool:
    s = str(s)
    result = False
    for char in s:
        if char == value:
            result = True

    return result
        

def main():
    data = {1, 2, 3, 'a', 'e', 'i', 'o', 'u', "red", "green", "blue"}
    check = input("What are you want to check : ")

    result = checkMembership(data, check)
    print(result)

main()