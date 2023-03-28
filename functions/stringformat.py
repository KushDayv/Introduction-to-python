""".format() function is used to format a selected part of a string
This can be used to add a part of a string to another

In string formatting you can either decide to use index numbers or use named indexes

for index numbers you have to specify the index of the item you want to format
for the named indexes you have to specify the content that the name of the index will hold in the
.format() function"""

quantity = input("Enter the number of items you want: ")
product_name = input("Enter the name of the product that you want: ")
enquiry = input("Enter the item you would want to know the cost: ")

txt = "I want {} of {} and how much does {} cost." 

print(txt.format(quantity, product_name, enquiry))



#formating the output to a certian number of decimal places

price = int(input("Enter the price of the product asked by the customer: "))
amount = input("Enter the amount of the product: ")

owner = "The Price of {} is {:.2f} Ksh." #the .2f will give the price to two decimal places

print(owner.format(amount,price))

