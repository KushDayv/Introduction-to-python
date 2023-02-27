"""Create a class named rectangle. initialize it with the length and width. Make two methods 
to return the area and perimeter"""
#A Program to calculate the area and the perimeter of a rectangle once you enter the length and width

length = int(input("Enter the length of the rectangle : "))
width = int(input("Enter the width of the rectangle : "))


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return length * width

    def perimeter(self):
        return 2 * (length + width)

a = Rectangle(length,width)         


print("The area of your rectangle is : ", a.area())
print("The perimeter of your rectangle is : ", a.perimeter())

        
