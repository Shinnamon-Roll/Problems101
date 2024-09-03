def isWordInList(word_list: list[str], search_term: str) -> bool:
    for word in word_list:
        if word == search_term:
            return True

def main():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    searchWord = input(f"{word_list}\nwhat word do you want to search : ")

    results = isWordInList(word_list, searchWord)
    print(results)

main()