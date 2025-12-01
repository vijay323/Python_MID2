"""Q9. Demonstrate polymorphism using a function that behaves differently for objects of Circle 
and Rectangle classes. Use private variables to show data hiding.""" 
import math 
 
class Circle: 
    def __init__(self, radius): 
        self.__radius = radius 
    def area(self): 
        return math.pi * self.__radius ** 2 
 
class Rectangle: 
    def __init__(self, length, width): 
        self.__length = length 
        self.__width = width 
    def area(self): 
        return self.__length * self.__width 
 
def show_area(shape): 
    print("Area:", shape.area()) 
 
show_area(Circle(5)) 
show_area(Rectangle(4, 6))
