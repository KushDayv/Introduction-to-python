#class to calculate the area of a circle

from math import pi
from math import pow

radius = int(input("Enter the radius of the circle : "))

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * pow(self.radius,2)    
    def perimeter (self):
        return pi * (2 * self.radius)
    
a = Circle(radius)
p = Circle(radius)    
print  ("The area of the circle is : ", a.area())    
print  ("The perimeter of the circle is : ", p.perimeter())    
    
