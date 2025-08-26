# Activity 2: Polymorphism

class Animal:
    def move(self):
        print("The animal moves on all fours.")

class Bird(Animal):
    def move(self):
        print("The bird flies by flapping its wings.")

class Fish(Animal):
    def move(self):
        print("The fish swims using its fins.")
class Reptile(Animal):
    def move(self):
        print("The reptile slithers on the ground.")

Animals = [Animal(), Bird(), Fish(), Reptile()]
for animal in Animals:
    animal.move()