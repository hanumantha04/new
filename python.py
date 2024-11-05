# List of students and their grades
students_grades = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78,
    'David': 92,
    'Eve': 88
}

# Calculate the average grade
total_grades = sum(students_grades.values())
num_students = len(students_grades)
average_grade = total_grades / num_students

# Prepare the results to be written to a text file
result = f"Average grade: {average_grade:.2f}\n\n"

result += "Grades of individual students:\n"
for student, grade in students_grades.items():
    result += f"{student}: {grade}\n"

# Write the result to a text file
with open('student_grades.txt', 'w') as file:
    file.write(result)

print("Results have been written to 'student_grades.txt'")
