# ==========================================
# Constructors in Python
# ==========================================

# A constructor is a special method
# that automatically executes when
# an object is created.

# ------------------------------------------
# Class Definition
# ------------------------------------------

class Student:

    # Constructor
    def __init__(self, name, course, roll_no):

        self.name = name
        self.course = course
        self.roll_no = roll_no

    # Method
    def display_info(self):

        print("\nStudent Information")
        print("-------------------")
        print(f"Name     : {self.name}")
        print(f"Course   : {self.course}")
        print(f"Roll No. : {self.roll_no}")


# ------------------------------------------
# Creating Objects
# ------------------------------------------

student1 = Student(
    "Shweta",
    "Artificial Intelligence and Data Science",
    101
)

student2 = Student(
    "Rahul",
    "Computer Engineering",
    102
)

# ------------------------------------------
# Calling Methods
# ------------------------------------------

student1.display_info()
student2.display_info()
