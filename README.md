# 🌸🐾 Object-Oriented Programming (OOP) Examples in Python

This project demonstrates **basic OOP concepts** in Python using two examples:
1. **Animals** → shows **Polymorphism**
2. **Flowers and Roses** → shows **Inheritance, Encapsulation, and Polymorphism**

---

## 🐾 Example 1: Polymorphism with Animals

### Code
```python
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
# OOP-Python-Week-5-Assignment
xplanation

All classes have a method move().

The behavior changes depending on the object (Bird, Fish, Reptile).

This is Polymorphism → “same name, different actions.”
# Parent class
class Flower:
    def __init__(self, name, color, petal_count=5, has_thorns=True):
        self.name = name
        self.color = color
        self.petal_count = petal_count
        self.has_thorns = has_thorns
        self.fragrance = "Mild"

    def describe(self):
        thorn_status = "has thorns" if self.has_thorns else "does not have thorns"
        return (f"{self.name} is a {self.color} rose with {self.petal_count} petals, "
                f"it {thorn_status} and has a {self.fragrance} fragrance.")

# Child class
class Rose(Flower):
    def __init__(self, name, color, petal_count=5, has_thorns=True):
        super().__init__(name, color, petal_count, has_thorns)
        self.fragrance = "Strong"   # Overridden attribute

    def describe(self):
        base_description = super().describe()
        return f"{base_description} It is known for its {self.fragrance} fragrance."

Rose1 = Rose("Madam Red", "red", 5, True)
print(Rose1.describe())

