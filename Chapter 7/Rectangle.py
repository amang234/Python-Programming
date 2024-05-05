# Write a Python class named Rectangle to represent a rectangle shape.
# The class should have the following functionalities:
# A method named set_dimensions that takes two parameters width and
# height and sets the attributes of the rectangle object accordingly.
# A method named area that calculates and returns the area of the
# rectangle
# A method named perimeter that calculates and returns the perimeter of
# the rectangle
# Use this to create objects of the class and print the width, height, area and
# perimeter.

class Rectangle:
    def set_dimensions(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width
    def perimeter(self):
        sum = self.height + self.width
        return 2 * sum

Rectangle1 = Rectangle()
Rectangle1.set_dimensions(2,4)
print(Rectangle1.height)
print(Rectangle1.width)
print(Rectangle1.area())
print(Rectangle1.perimeter())