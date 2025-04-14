#  Polymorphism Example with Animals

class Animal:
    def move(self):
        print("Moving...")

class Dog(Animal):
    def move(self):
        print(" Running on four legs!")

class Bird(Animal):
    def move(self):
        print("Flying in the sky!")

class Fish(Animal):
    def move(self):
        print(" Swimming in the water!")

# Example usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
