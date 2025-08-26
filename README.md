
# 🌟 Object-Oriented Programming (OOP) Examples in Python

This repository contains Python examples that demonstrate the **core OOP concepts**:

- **Inheritance**
- **Encapsulation**
- **Polymorphism**

---

## 🐾 Example 1: Polymorphism (Animals)

This example shows how the same method `move()` behaves differently depending on the object:

- `Animal` → moves on all fours  
- `Bird` → flies by flapping wings  
- `Fish` → swims using fins  
- `Reptile` → slithers on the ground


### 📌 Code
```python
# Polymorphism Example: Animals

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

# Demonstration of polymorphism
Animals = [Animal(), Bird(), Fish(), Reptile()]
for animal in Animals:
    animal.move()


 Red", "red", 5, True)
print(Rose1.describe())

