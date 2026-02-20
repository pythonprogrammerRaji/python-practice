# Implement a Shape class and derive Circle and Rectangular classes with a method Calculate_area.
# Each class shoud calcalute area differentlty based on its shape. Create a loop to calculate areas
# both circle and Rectangle objects

class Shape:
    def calculate_area(self):
        print("Shape Calculated")
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def calculate_area(self):
        print(3.14 * self.r * self.r)
class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        print(self.base * self.height)

s = [Circle(5), Rectangle(2,5)]

for shape in s:
    shape.calculate_area()