############################################################
#Midterm2B
#
#Course: CMPT 140 Introduction to Computing Science and Programming 1
#Instructor: Dr.Herbert H.Tsang 
#Description: This is a simple python game that allows the user to guess a number and then it compares from the number generated 
#Due date: 2023/03/31
#
#Author:  
#Input: 56
#Output: The number is too low!
#I pledge that I have completed the programming assignment independently.
#I have not copied from a student of any source
#I have not given my code to any student
#
#sign here:


from numpy import random

winning_number = random.randint(0,100)

num = int(input("Guess any number :"))

if num == winning_number:
    print("You are right and Good Job!!!")
elif num < winning_number:
    print("The value is too low")    
elif num > winning_number:
    print("The value is too high")
        