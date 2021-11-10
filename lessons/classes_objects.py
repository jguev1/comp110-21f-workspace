"""Example of a class and object instantiation"""

# classes start with uppercase letter
class Pizza:
    """Modeling the idea of a Pizza."""

    # Attribute Definitions
    size: str 
    toppings: int 
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
            """Constructor defenition for initialization of attributes"""
            self.size = size
            self.toppings = toppings

    def price(self, tax: float) -> float:
        """Calculare the prince of a Pizza"""
        total: float =0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8

        total += self.toppings *.75

        if self.extra_cheese:
            total += 1

        total *= tax

        return total


a_pizza: Pizza = Pizza("large", 3)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(a_pizza.size)
print(another_pizza.size)
print(another_pizza.price(1.05))