from typing import List

def calculate_gpa(grades: List[int]) -> float:
    grade_points = [
        4.0 if 80 <= g <= 100 else
        3.5 if 75 <= g <= 79 else
        3.0 if 70 <= g <= 74 else
        2.5 if 65 <= g <= 69 else
        2.0 if 60 <= g <= 64 else
        1.5 if 55 <= g <= 59 else
        1.0 if 50 <= g <= 54 else
        0.0 for g in grades
    ]
    
    return round(sum(grade_points) / len(grade_points), 2)

def main():
    # Input grades
    grades = list(map(int, input("Enter grades for 5 subjects separated by spaces: ").split()))
    
    if len(grades) != 5:
        print("Please enter exactly 5 grades.")
        return
    
    # Calculate GPA
    gpa = calculate_gpa(grades)
    
    # Print the GPA
    print(f"GPA: {gpa}")

if __name__ == "__main__":
    main()
