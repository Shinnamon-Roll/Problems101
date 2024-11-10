def storeStudentInfo(student_data: list[tuple[str, str]]) -> dict[str, str]:
    studentDict = {}

    for studentID, nickname in student_data:
        studentDict[studentID] = nickname

    return studentDict

def main():
    data = []

    for _ in range(3):
        studentID = int(input("Enter Student ID : "))
        nickname = input("Enter nickname : ")
        data.append((studentID, nickname))

    result = storeStudentInfo(data)
    print(result)
    
main()