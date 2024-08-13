from typing import Tuple

def separateByIndex(s: str) -> Tuple[str, str]:
    evenChar = ""
    oddChar = ""

    for count, value in enumerate(s):
        if count % 2 == 0 or count == 0:
            evenChar += value
        elif count % 2 == 1 or count == 1:
            oddChar += value
        else:
            print("Error")
    print(f'Even Indexes Characters : "{evenChar}"\nOdd Indexes Characters : "{oddChar}"')

def main():
    words = input("type words for make even and odd : ")
    separateByIndex(words)

main()