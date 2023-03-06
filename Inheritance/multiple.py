#A program to show multiple inheritance in python

name = input("Enter the name of the owner institution of the car : ")
model = input("Enter the model of the car : ")
color = input("Enter the color of the car : ")
engine = input("Enter the engine size of the vehicle : ")





class Car:
    def __init__(self,name,model,color,engine):
        self.model = model
        self.color = color
        self.engine = engine
        self.name = name
 
class Owner:
    def person(self):
        return name



class Institution(Car,Owner):
    def zetech(self):
        return (model,color,engine)
    
F = Institution(name,model,color,engine)
print("The Car Details are (model,color,engine) : ",F.zetech())   
print("The car belongs to : ",F.person())
