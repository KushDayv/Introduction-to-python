#This is a simple python game.
from numpy import random

winning_number = random.randint(0,50)
num = int(input("Guess any number :"))
if num == winning_number:
    print("YOU WIN!!!")
elif num < winning_number:
    print("The value is too low")    
elif num > winning_number:
    print("The value is too high")
        