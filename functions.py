"""Types of functions
a.User-defined functions
b.Built-in functions
c.Lambda functions
d.Recursion functions

syntax
def my_function(): #the def keyword is used")"""

#Function to return the area of a circle(area of a circle = pi * (r*r))

from math import pi
from math import pow

radius = int(input("Enter the radius of a circle :"))
radius = int(input("Enter the radius of a cylinder :"))
radius = int(input("Enter the radius of a sphere :"))
length = int(input("Enter the length of the cylinder :"))


def area_of_circle(radius):
    area = pi * pow(radius, 2)
    return area

print("The area of the circle is :",area_of_circle(radius))

#Function to calculate the volume of a cylinder(volume = cross-sectional area * length)

def volume_of_cyclinder(radius,length):
    cross_sectional_area = pi * pow(radius, 2)
    volume = cross_sectional_area * length
    return volume

print("The volume of the cylinder is : ", volume_of_cyclinder(radius,length))

#Functions to calculate the volume of a sphere

def volume_of_sphere(radius):
    volume = 4/3 * (pi * pow(radius, 3))
    return volume

print("The volume of the sphere is : ", volume_of_sphere(radius))

"""The volume of a sphere 
Function to calculate the compund interest """
