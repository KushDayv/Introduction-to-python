"""Types of functions
a.User-defined functions
b.Built-in functions
c.Lambda functions
d.Recursion functions

syntax
def my_function(): #the def keyword is used")
    """

#Function to return the area of a circle(area of a circle = pi * (r*r))

from math import pi
from math import pow

radius1 = int(input("Enter the radius of a circle :"))
radius2 = int(input("Enter the radius of a cylinder :"))
radius3 = int(input("Enter the radius of a sphere :"))
length = int(input("Enter the length of the cylinder :"))


def area_of_circle(radius1):
    area = pi * pow(radius1, 2)
    return area

print("The area of the circle is :",area_of_circle(radius1))

#Function to calculate the volume of a cylinder(volume = cross-sectional area * length)

def volume_of_cyclinder(radius2,length):
    cross_sectional_area = pi * pow(radius2, 2)
    volume = cross_sectional_area * length
    return volume

print("The volume of the cylinder is : ", volume_of_cyclinder(radius2,length))

#Functions to calculate the volume of a sphere

def volume_of_sphere(radius3):
    volume = 4/3 * (pi * pow(radius3, 3))
    return volume

print("The volume of the sphere is : ", volume_of_sphere(radius3))

