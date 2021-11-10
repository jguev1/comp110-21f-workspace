"""Example of a Point class"""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y
    
    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor"""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point"""
        #x: float = self.x * factor
        #y: float = self.y * factor
        #scaled_point: Point = Point(x,y)
        #return scaled_point
        #OR
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """Produce a str representation of a Point for humans"""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, rhs: Point) -> Point:
        print(" add was called")
        return Point(self.x + rhs.x, self.y + rhs.y)
 


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
#print(b)
#or instead of print(b)
#b_as_a_str: str = str(b)
#print(b_as_a_str)
