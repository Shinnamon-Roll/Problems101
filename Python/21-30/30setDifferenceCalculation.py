def calculateSetDifferences(set1: set, set2: set) -> tuple[set, set]:
    result1 = set1.difference(set2)
    result2 = set2.difference(set1)
    return result1, result2

def main():
    set1 = {'a', 'b', 'c'}
    set2 = {'b', 'c', 'd'}
    
    result = calculateSetDifferences(set1, set2)
    print(result)

main()