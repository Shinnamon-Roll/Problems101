def insertAtFront(words: list[str]) -> list[str]:
    wordList.insert(0, words)
    return wordList

def main():
    while True:
        word = input("Enter word o insert : ")
        results = insertAtFront(word)
        print(results)

        check = input("Again? (yes or no) : ")
        if check == "no":
            break
        
wordList = []
main()