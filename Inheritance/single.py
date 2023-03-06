"""
Data abstraction - data hiding
Encapsulation - wrapping of data
Polymophism - taking many forms
"""
#A program to show single inheritance in python

class Animal:
    def legs(self):
        print("I have four legs")

    def fur(self):
        print("My body is covered with fur")

class Dog(Animal):  #class Dog inherits from the class animal
    def bark(self):
        print("The dog barks")




d = Dog()
d.legs()
d.fur()
d.bark()            

