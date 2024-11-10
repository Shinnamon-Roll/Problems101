def removeWordFromList(words: list[str], word: str) -> list[str]:
    wordList = words

    for cum in wordList:
        if cum == word:
            wordList.remove(cum)
    
    return wordList

def main():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    while True:
        wordRemove = input(f"{words}\nWhat words do you want to remove : ")
        results = removeWordFromList(words, wordRemove)
        print(f"\n{results}\nRemoved < {wordRemove} >\n")

        check = input("Again? (yes or no): ")
        if check == "no":
            break

main()