def insertAtFront(words: list[str]) -> list[str]:
    for word in words:
        print(word)


    print(words)

def main():
    strings = input("Enter your words : ").split()
    results = insertAtFront(strings)
    print(results)

main()