def isWordInList(word_list: list[str], search_term: str) -> bool:
    for word in word_list:
        if word == search_term:
            return True
        else:
            return False

def main():
    wordList = []
    for i in range(10):
        inputword = input(f"{wordList}\nenter your word to add in list : ")
        wordList.append(inputword)

    searchWord = input(f"{wordList}\nwhat word do you want to search : ")
    results = isWordInList(wordList, searchWord)
    print(results)

main()