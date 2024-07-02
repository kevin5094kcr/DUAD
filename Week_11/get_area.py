import math # We need this module in order to use the value of π

class Circle:
    def __init__(self, radius):
        self.radius = radius 

    def get_area(self):
        return math.pi * (self.radius **2)

circle = Circle(7)

area = circle.get_area()

print(f"The area of the circle with radius {circle.radius} is {area}")