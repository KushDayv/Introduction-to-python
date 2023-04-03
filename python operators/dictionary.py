"""This is a program that allows one to enter the name of products and their prices and 
then when the user is done, the output is stored in a dictionary"""


prices = {}

#The loop will iterate until the user enters the word done so as to end the loop
while True:  
    name = input("Enter name of item (or 'done' to exit): ")
    if name == 'done':
        break
    price = float(input("Enter price of item: "))
    prices[name] = price

print(prices)
