def enter_student():
    student = {}
    student['name'] = input("Enter the student's full name: ")
    student['section'] = input("Enter the student's section: ")
    student['spanish'] = get_valid_grade("Spanish")
    student['english'] = get_valid_grade("English")
    student['social_studies'] = get_valid_grade("Social Studies")
    student['science'] = get_valid_grade("Science")
    return student


def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def view_students(students):
    if not students:
        print("No student data available.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Section: {student['section']}, ")
            print(f"Spanish: {student['spanish']}, English: {student['english']}, ")
            print(f"Social Studies: {student['social_studies']}, Science: {student['science']}")


def calculate_average_grade(student):
   total = student['spanish'] + student['english'] + student['social_studies'] + student['science']

   average = total / 4

   return average


def view_top_3_students(students):
    if len(students) < 1:
        print("Not enough students to display top 3.")
    else:
        students_sorted = sorted(students, key=calculate_average_grade, reverse=True) # reverse=True Order from highest to lowest
        top_3_students = students_sorted[:3]
        for student in top_3_students:
            avg_grade = calculate_average_grade(student)
            print(f"Name: {student['name']}, Average Grade: {avg_grade:.2f}") # Formatted in 2 decimals


def view_average_grade(students):
    if not students:
        print("No student data available.")
    else:
        total_avg = sum(calculate_average_grade(s) for s in students) / len(students)
        print(f"Average grade of all students: {total_avg:.2f}") # Formatted in 2 decimals
