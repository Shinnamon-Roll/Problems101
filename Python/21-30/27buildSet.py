def buildSet() -> set[int]:
    mySet = set()
    count = 0
    while True:
        data = int(input("Enter the number for make set : "))
        mySet.add(data)
        count += 1
        if count == 5:
            print(sorted(mySet))
            mySet = set()
            count = 0

        if data == "done" or data == "Done":
            break

buildSet()
