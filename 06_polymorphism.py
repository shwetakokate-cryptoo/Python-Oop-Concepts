# ==========================================
# Polymorphism in Python
# ==========================================

# Polymorphism allows the same method
# to have different implementations.

# ------------------------------------------
# Class Definitions
# ------------------------------------------

class Dog:

    def sound(self):
        print("Dog says: Bark 🐶")


class Cat:

    def sound(self):
        print("Cat says: Meow 🐱")


class Cow:

    def sound(self):
        print("Cow says: Moo 🐄")


# ------------------------------------------
# Function Using Polymorphism
# ------------------------------------------

def animal_sound(animal):

    animal.sound()


# ------------------------------------------
# Creating Objects
# ------------------------------------------

dog = Dog()
cat = Cat()
cow = Cow()

# ------------------------------------------
# Calling Function
# ------------------------------------------

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
