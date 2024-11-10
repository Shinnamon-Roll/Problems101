def setOperations(set1: set, set2: set) -> tuple[set, set]:
    return f"{set1 | set2}{set1 & set2}"

def main():
    set1 = {'a', 'e', 'i', 'o', 'u'}
    set2 = {'h', 'e', 'l', 'l', 'o'}

    result = setOperations(set1, set2)
    print(result)

main()