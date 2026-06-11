# ==========================================
# Hierarchical Inheritance in Python
# ==========================================

# One Parent Class
# Multiple Child Classes

# ------------------------------------------
# Parent Class
# ------------------------------------------

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display_person(self):

        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# ------------------------------------------
# Child Class 1
# ------------------------------------------

class Student(Person):

    def __init__(self, name, age, course):

        super().__init__(name, age)

        self.course = course

    def display_student(self):

        print("\nStudent Information")
        print("-------------------")

        self.display_person()
        print(f"Course : {self.course}")


# ------------------------------------------
# Child Class 2
# ------------------------------------------

class Teacher(Person):

    def __init__(self, name, age, subject):

        super().__init__(name, age)

        self.subject = subject

    def display_teacher(self):

        print("\nTeacher Information")
        print("-------------------")

        self.display_person()
        print(f"Subject : {self.subject}")


# ------------------------------------------
# Creating Objects
# ------------------------------------------

student1 = Student(
    "Shweta",
    18,
    "Artificial Intelligence and Data Science"
)

teacher1 = Teacher(
    "Patil Sir",
    40,
    "Python Programming"
)

# ------------------------------------------
# Calling Methods
# ------------------------------------------

student1.display_student()

teacher1.display_teacher()
