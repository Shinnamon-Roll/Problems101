from typing import List, Dict

def countWordOccurrences(words: List[str]) -> Dict[str, int]:
    wordCount = {}
    
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    
    return wordCount

def main():
    words = input("Enter a sequence of words: ").split()
    result = countWordOccurrences(words)
    print(result)

main()
