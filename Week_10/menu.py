from actions import enter_student, view_students, view_top_3_students, view_average_grade
from data import export_to_csv, import_from_csv


def show_menu():
    students = []  # Guarda los estudiantes ingresados en una lista 
    while True:
        print("Menu:")  
        print("1. Enter student information")
        print("2. View all students")
        print("3. View top 3 students by average grade")
        print("4. View average grade of all students")
        print("5. Export data to CSV")
        print("6. Import data from CSV")
        print("7. Exit")

        choice = input("Choose an option: ")  

        if choice == '1':
            student = enter_student()  
            students.append(student)  
        elif choice == '2':
            view_students(students)   
        elif choice == '3':
            view_top_3_students(students)  
        elif choice == '4':
            view_average_grade(students)  
        elif choice == '5':
            export_to_csv(students)  
        elif choice == '6':
            students = import_from_csv()  
        elif choice == '7':
            print("Exiting the program.")  
            break
        else:
            print("Invalid choice. Please try again.") # Error message in case the user types a word instead of a number