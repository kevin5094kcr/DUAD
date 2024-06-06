import csv

def export_to_csv(students):
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Section', 'Spanish', 'English', 'Social Studies', 'Science'])
        for student in students:
            writer.writerow([student['name'], student['section'], student['spanish'], student['english'], student['social_studies'], student['science']])
    print("Data exported to students.csv")

def import_from_csv():
    try:
        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                student = {
                    'name': row['Name'],
                    'section': row['Section'],
                    'spanish': float(row['Spanish']),
                    'english': float(row['English']),
                    'social_studies': float(row['Social Studies']),
                    'science': float(row['Science'])
                }
                students.append(student)
            print("Data imported from students.csv")
            return students
    except FileNotFoundError:
        print("No CSV file found.")
        return []