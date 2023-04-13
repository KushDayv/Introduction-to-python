
#A program that will double the items in the list as it prints them
words = ['apple', 'banana', 'orange', 'grape']

doubled_words = []

for word in words:
    doubled_words.append(word)
    doubled_words.append(word)

print(doubled_words)


# A program to check for the discount of a user once he or she has entered the number of items purchased
quantity = int(input("Enter a quantity: "))  

total = quantity * 100

if total > 1000:
    discount = 0.1 * total
    total_cost = total - discount

    print("Your discount is: ", discount)
    print("Your total price that you will pay is: ", total_cost)

else:
    print("No discount, You will pay: ",total)   


"""In this program the quantity is taken as the number of items that the customer is buying
based on the fact that each item costs 100,,,,,so you multiply the quantity entered and then multiply
with 100 and from there calculate whether the customer will get discount or not """
