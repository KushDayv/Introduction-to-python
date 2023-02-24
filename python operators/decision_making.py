"""Write a program that will print the largest number
of the three numbers. Prompt the user to enter the three numbers"""
num0 = int(input("Enter the first number :"))
num1 = int(input("Enter the second number :"))
num2 = int(input("Enter third number :"))

if (num0 > num1 and num0 > num2):
    print("The number :",num0, "is the largest of them all")
elif (num1 > num0 and num1 > num2):
    print("The number :",num1, "is the largest of them all")
elif (num2 > num0 and num2 > num1):
    print("The number :",num2, "is the largest of them all")
else:
    print("Invalid comparison")    
   

