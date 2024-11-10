def searchCountriesByLetter(countryData: dict[str, str], letter: str) -> list[str]:
    listResult = []

    for value in countryData.values():
        for word in value.split(':', 1):
            for char in word:
                if letter == char:
                    listResult.append(word)
    
    return listResult
        

def main():
    countryData = {
        "+1": "United States",
        "+44": "United Kingdom",
        "+91": "India",
        "+81": "Japan",
        "+49": "Germany",
        "+86": "China"
    }

    # letter = input("Enter char for seach : ")
    letter = "I"

    result = searchCountriesByLetter(countryData, letter)
    print(result)

main()