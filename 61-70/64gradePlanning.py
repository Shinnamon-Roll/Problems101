def calculate_required_grades(current_gpa: float, target_gpa: float, credits: list[int]) -> list[str]:
    total_credits = sum(credits)
    current_points = current_gpa * total_credits
    target_points = target_gpa * total_credits
    grade_points_needed = target_points - current_points
    grade_points = {'A': 4, 'B+': 3.5, 'B': 3, 'C+': 2.5, 'C': 2, 'D+': 1.5, 'D': 1}
    grades = []

    for credit in credits:
        for grade, points in grade_points.items():
            if points * credit >= grade_points_needed / len(credits):
                grades.append(grade)
                grade_points_needed -= points * credit
                break

    return grades

def main():
    current_gpa = float(input("Enter your current GPA: "))
    target_gpa = float(input("Enter your target GPA: "))
    credits = list(map(int, input("Enter credit hours for 5 courses (space-separated): ").split()))
    result = calculate_required_grades(current_gpa, target_gpa, credits)
    print("Minimum grades required: ", result)

main()
