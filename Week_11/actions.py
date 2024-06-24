from student import Student

def enter_student():
    name = input("Enter the student's full name: ")
    section = input("Enter the student's section: ")
    spanish = get_valid_grade("Spanish")
    english = get_valid_grade("English")
    social_studies = get_valid_grade("Social Studies")
    science = get_valid_grade("Science")

    return Student(name, section, spanish, english, social_studies, science)


def get_valid_grade(subject):
    while True:
        try: 
            grade= float(input(f"Enter the grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def view_students(students):
    if not students:
        print(" No student data available.")
    else:
        for student in students:
            print(f"Name: {student.name}, Section: {student.section}")
            print(f"Spanish: {student.spanish}, English: {student.english}")
            print(f"Social Studies: {student.social_studies}, Science: {student.science}")


def calculate_average_grade(student):
    return student.calculate_average()

def view_top_3_students(students):
    if len(students) <= 1:
        print("Not enough students to display top 3.")
    else: 
        students_sorted = sorted(students, key=calculate_average_grade, reverse=True)
        top_3_students = students_sorted[:3]
        for student in top_3_students:
            avg_grade = student.calculate_average()
            print(f"Name:{student.name}, Average Grade: {avg_grade: .2f}")

def view_average_grade(students):
    if not students:
        print("No student data available.")
    else:
        total_avg = sum(student.calculate_average() for student in students) / len(students)
        print(f"Average grade of all students: {total_avg: .2f}")