class Student:
    def __init__(self, roll_no, name, department):
        self.roll_no = roll_no
        self.name = name
        self.department = department
class StudentManagement:
    def __init__(self):
        self.students = []
    def add_student(self):
        roll = input("Enter roll number: ")
        if any(s.roll_no == roll for s in self.students):
            print("Roll number already exists!")
            return
        name = input("Enter student name: ")
        department = input("Enter department: ")
        student = Student(roll, name, department)
        self.students.append(student)
        print("Student added successfully!")
    def view_students(self):
        if not self.students:
            print("No students available!")
            return
        for s in self.students:
            print("\nRoll Number:", s.roll_no)
            print("Name:", s.name)
            print("Department:", s.department)
    def search_student(self):
        roll = input("Enter roll number: ")
        for s in self.students:
            if s.roll_no == roll:
                print("Student Found!")
                print("Name:", s.name)
                print("Department:", s.department)
                return
        print("Student not found!")
    def delete_student(self):
        roll = input("Enter roll number: ")
        for s in self.students:
            if s.roll_no == roll:
                self.students.remove(s)
                print("Student deleted successfully!")
                return
        print("Student not found!")
system = StudentManagement()
while True:
    print("\n--- STUDENT MANAGEMENT ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        system.add_student()
    elif choice == "2":
        system.view_students()
    elif choice == "3":
        system.search_student()
    elif choice == "4":
        system.delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
