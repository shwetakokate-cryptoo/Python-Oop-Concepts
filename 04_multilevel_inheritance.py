# ==========================================
# Multilevel Inheritance in Python
# ==========================================

# Person -> Student -> GraduateStudent

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

        super().__init__(name, age)

        self.course = course

    def display_student(self):

        print("\nStudent Information")
        print("-------------------")
        print(f"Course : {self.course}")


# ------------------------------------------
# Grandchild Class
# ------------------------------------------

class GraduateStudent(Student):

    def __init__(
        self,
        name,
        age,
        course,
        specialization
    ):

        super().__init__(name, age, course)

        self.specialization = specialization

    def display_graduate_student(self):

        print("\nGraduate Student Information")
        print("----------------------------")
        print(f"Specialization : {self.specialization}")


# ------------------------------------------
# Creating Object
# ------------------------------------------

student1 = GraduateStudent(
    "Shweta",
    18,
    "Artificial Intelligence and Data Science",
    "Machine Learning"
)

# ------------------------------------------
# Calling Methods
# ------------------------------------------

student1.display_person()
student1.display_student()
student1.display_graduate_student()
