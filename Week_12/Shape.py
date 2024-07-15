from abc import ABC, abstractmethod 

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

import math 

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius
    
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side 


    def calculate_perimeter(self):
        return 4 * self.side
    
    
    def calculate_area(self):
        return self.side ** 2
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height 


    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    

    def calculate_area(self):
        return self.width * self.height
        

circle = Circle(6)
square = Square(4)
rectangle = Rectangle(3, 6)

print("Circle perimeter:", circle.calculate_perimeter())
print("Circle area:", circle.calculate_area())

print("Square perimeter:", square.calculate_perimeter())
print("Square area:", square.calculate_area())

print("Rectangle perimeter:", rectangle.calculate_perimeter())
print("Rectangle area:", rectangle.calculate_area())