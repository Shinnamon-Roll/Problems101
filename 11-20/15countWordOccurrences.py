from typing import List, Dict

def countWordOccurrences(words: List[str]) -> Dict[str, int]:
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def main():
    words = input("Enter a sequence of words: ").split()
    
    result = countWordOccurrences(words)
    
    print(result)

main()
