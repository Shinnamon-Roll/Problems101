def collectUniqueWords(wordsList):
    words = []
    count = 0
    for word in wordsList:
        if word not in words:
            words.append(word)
            count += 1
        if count == 5:
            break
    return words

def main():
    stringList = []
    while True:
        strings = input("Please enter a string (one by one, press Enter to stop): ")
        if strings == '':
            break
        stringList.append(strings)
    
    result = collectUniqueWords(stringList)
    print(f"Output is : {result}")

main()
