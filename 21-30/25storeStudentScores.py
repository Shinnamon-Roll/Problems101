def storeStudentScores(studentData: list[tuple[str, str, float]]) -> dict[str, dict[str, float]]:
    
    result = {
        student_id: {"name": name, "score": score}
        for student_id, name, score in studentData
    }
    return result    


def main():
    data = []

    for _ in range(3):
        studentID = int(input("Enter Student ID : "))
        nickname = input("Enter nickname : ")
        score = int(input("Score : "))
        data.append((studentID, nickname, score))

    result = storeStudentScores(data)

    print(result)

main()