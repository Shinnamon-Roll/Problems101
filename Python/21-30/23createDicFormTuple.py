def createDictionary(tuple1: tuple[int, ...], tuple2: tuple[str, ...]) -> dict[int, str]:
    dict = {}
    number = 0
    
    for i in tuple2:
        if i == "done":
            break
        dict[number] = i
        number += 1

    return dict

def main():
    list1 = []
    list2 = []
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    number = 1

    while True:
        word = input("Enter a word for list (done for stop) : ")
        list1.append(number)
        list2.append(word)
        number += 1

        if word == "done":
            break 
        if len(list1) > 100:
            break

    result = createDictionary(tuple1, tuple2)
    print(result)

main()