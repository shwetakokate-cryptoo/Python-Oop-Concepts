# ==========================================
# Inheritance in Python
# ==========================================

# Inheritance allows one class
# to inherit properties and methods
# from another class.

# ------------------------------------------
# Parent Class
# ------------------------------------------

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display_person(self):

        print("\nPerson Information")
        print("------------------")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# ------------------------------------------
# Child Class
# ------------------------------------------

class Student(Person):

    def __init__(self, name, age, course):

        # Call Parent Constructor
        super().__init__(name, age)

        self.course = course

    def display_student(self):

        print("\nStudent Information")
        print("-------------------")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")


# ------------------------------------------
# Creating Object
# ------------------------------------------

student1 = Student(
    "Shweta",
    18,
    "Artificial Intelligence and Data Science"
)

# ------------------------------------------
# Calling Methods
# ------------------------------------------

student1.display_person()
student1.display_student()
