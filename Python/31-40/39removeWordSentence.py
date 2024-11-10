def removeWord(sentence: str, wordToRemove: str) -> str:
    if wordToRemove in sentence:
        newSentence = ' '.join(sentence.split()).replace(wordToRemove, '').replace("  ", " ").strip()
        print(f"Updated sentence: {newSentence}")
        return newSentence
    else:
        print("Warning: wordToRemove is not in the sentence")
        return sentence

def main():
    data = input("Enter a sentence: ")
    check = True
    while check:
        wordToRemove = input("Remove word: ")
        if wordToRemove.lower() == 'exit':
            print(data)
            print("Exiting...")
            check = False
        else:
            data = removeWord(data, wordToRemove)

main()
