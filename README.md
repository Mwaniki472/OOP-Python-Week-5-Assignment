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

