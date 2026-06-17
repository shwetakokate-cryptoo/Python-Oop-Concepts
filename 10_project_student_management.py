# ==========================================
# Student Management System
# ==========================================

# Mini OOP Project

# ------------------------------------------
# Student Class
# ------------------------------------------

class Student:

    def __init__(self, roll_no, name, course):

        self.roll_no = roll_no
        self.name = name
        self.course = course

    def display(self):

        print("\n-----------------------------")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Course  : {self.course}")
        print("-----------------------------")


# ------------------------------------------
# Student Management System
# ------------------------------------------

students = []


def add_student():

    print("\nAdd New Student")

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    student = Student(
        roll_no,
        name,
        course
    )

    students.append(student)

    print("\nStudent added successfully.")


def view_students():

    if len(students) == 0:
        print("\nNo student records found.")
        return

    print("\nStudent Records")

    for student in students:
        student.display()


def search_student():

    roll_no = input(
        "\nEnter Roll Number to Search: "
    )

    for student in students:

        if student.roll_no == roll_no:

            print("\nStudent Found")
            student.display()
            return

    print("\nStudent not found.")


# ------------------------------------------
# Main Menu
# ------------------------------------------

def main():

    while True:

        print("\n================================")
        print(" STUDENT MANAGEMENT SYSTEM ")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("\nThank you!")
            break

        else:
            print("\nInvalid choice.")


# ------------------------------------------
# Run Program
# ------------------------------------------

main()
