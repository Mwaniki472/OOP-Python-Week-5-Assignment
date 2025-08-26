#Assignment 1 Object Oriented Programming (OOP)

#Parent class 

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
        self.fragrance = "Strong"

    def describe(self):
        base_description = super().describe()
        return f"{base_description} It is known for its {self.fragrance} fragrance."

Rose1 = Rose("Madam Red", "red", 5, True)
print(Rose1.describe())



