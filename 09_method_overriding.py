# ==========================================
# Method Overriding in Python
# ==========================================

# Method overriding occurs when a child class
# defines a method with the same name as
# the method in the parent class.

# ------------------------------------------
# Parent Class
# ------------------------------------------

class Animal:

    def sound(self):

        print("Animals make different sounds.")


# ------------------------------------------
# Child Class
# ------------------------------------------

class Dog(Animal):

    # Overriding Parent Method
    def sound(self):

        print("Dog says: Bark 🐶")


# ------------------------------------------
# Child Class
# ------------------------------------------

class Cat(Animal):

    # Overriding Parent Method
    def sound(self):

        print("Cat says: Meow 🐱")


# ------------------------------------------
# Creating Objects
# ------------------------------------------

animal = Animal()
dog = Dog()
cat = Cat()

# ------------------------------------------
# Calling Methods
# ------------------------------------------

animal.sound()

dog.sound()

cat.sound()
