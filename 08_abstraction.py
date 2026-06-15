# ==========================================
# Abstraction in Python
# ==========================================

# Abstraction hides implementation details
# and shows only the required functionality.

from abc import ABC, abstractmethod


# ------------------------------------------
# Abstract Class
# ------------------------------------------

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# ------------------------------------------
# Child Class 1
# ------------------------------------------

class Car(Vehicle):

    def start(self):
        print("Car starts using a key.")


# ------------------------------------------
# Child Class 2
# ------------------------------------------

class Bike(Vehicle):

    def start(self):
        print("Bike starts using a self-start button.")


# ------------------------------------------
# Creating Objects
# ------------------------------------------

car = Car()
bike = Bike()

# ------------------------------------------
# Calling Methods
# ------------------------------------------

car.start()
bike.start()
