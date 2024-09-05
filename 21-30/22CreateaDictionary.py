def createDictionary(list1:list[int],list2:list[str]) -> dict[int, str]:   
    dict = {}
    value = 0
    
    for key in list1:
        if list2[value] == "done":
            break
        dict[key] = list2[value]
        value += 1
        
    print(dict)

def main():
    list1 = []
    list2 = []
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

    createDictionary(list1, list2)
    
main()
