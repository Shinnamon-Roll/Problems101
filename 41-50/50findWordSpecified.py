def findWordsOfLength(words: list[str], length: int) -> list[str]:
    result = []
    for word in words:
        if length == len(word):
            result.append(word)

    return result

def main():
    inputWords = ["apple", "banana", "cherry", "date", "fig", "grape"]
    length = 5

    result = findWordsOfLength(inputWords, length)
    print(result)

main()