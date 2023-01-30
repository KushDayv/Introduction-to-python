#python operators
"""types of operators include
1.Arithmetic operators
2.Assignment operators
3.Comparison operators
4.Logical operators
5.Relational operators
6.Identity operators
7.Bitwise operators
8.Membership operators
"""
###ARITHMETIC OPERATORS###
print("Arithmetic operators")
"""The program show show how to use different operators 
They include:
addition +
subtraction -
multiplication *
division(float) /
division(floor) //
modulus %"""

a = 33
b = 7

#addition  
print(a+b)

#subtraction
print(a-b)

#multiplication
print(a*b)

#division float....gives the answer as a float value
print(a/b)

#division floor....gives the answer as an integer by roundibg down
print(a//b)

#modulus
print("Modulus of a number",a%b)

""" A program that test the divisibility test and whether the number is even"""

print("To check whether the number is even or not")
a = int(input("Enter any number:"))

if (a%2 == 0):
    print("The number is even")

else:
    print("The number is not even")

#to check whether the same entered number is divisible by 5
print("To check the divisibility test")

if (a%5 == 0):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")



    """Write a program to assign a discount of 5%
if amount to purchase exceeds sh 1,000"""

total_price = float(input("Enter the total amount of the total goods:"))

discount = 5/100 * total_price

if (total_price >= 1000):
    print("The discount offered is :", discount)

else:
    print("No discount given")    


###RELATIONAL OPERATORS###
#they compare the values and return true or false
print("Relational operators")
"""They are:
greater than >
less than <
equal to ==
not equal to !=
greater than or equal to >=
less than or equal to <=
"""

x = 12
y = 5
z = 12

#greater than
print(x>y)

#less than
print(x<y)

#equal to
print(x==z)

#not equal to 
print(x!=y)

#greater than or equal to 
print(x>=y)
print(x>=z)

#less than or equal to
print(x<=y)
print(x<=z)

"""Write a program to assign a discount of 5%
if amount to purchase esceeds sh 1,000"""

total_price = float(input("Enter the total amount of the total goods:"))

discount = 5/100 * total_price

if (total_price >= 1000):
    print("The discount offered is :", discount)

else:
    print("No discount given")    



#LOGIC OPERATORS
print("Logical operators")
"""They include
and 
or 
not"""
k = 5
j = 4
l = 5

#and
print(j and j)
print(k and l)

#or
print(k or j)
print(k or l)


#not
print(k or j)
print(k or l)


"""Write a program to check if a person is eligibel to vote. The person must be
a Kenyan citizen and above 18 years."""

nationality = str(input("Are you a Kenyan citizen ?")).lower

age = int(input("Enter you current age :"))

if (nationality == 'yes' and age >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")    



"""Write a program to implement the following requirements:
A bank will offer  a customer a loan if they  are 21  years or over and have an annual 
  income of at least Sh 21,000. The customer age and income are input in response to user friendly
  prompts. Write a program that will output the following:
  
  1.Congratulations you qualify for a loan
  2.Unfortunately, we are unable to offer you a loan at this time."""

age  = int(input("Enter your age :"))

annual_income = float(input("Enter your annual income :"))

debt = input("Do you have any existing debt ?").lower()


if (age >= 21 and annual_income >= 21000 and debt == 'no'):
    print("Congratualtions you qualify for a loan")
else:
    print("Unfortunately, we are unable to offer you a loan at this time")


    """Write a program to check if you are eligible to vote:

Must be an East African citizen (Kenya, Uganda, Tanzania)and above 18 years"""

requirements = ["kenya", "uganda", "Tanzania"]

voter = input("Enter you nationality :").lower

age = int(input("Enter your age :"))

if (voter in requirements and age >= 18):
    print("Eligible to vote")
else:
    print("You are not eligible to vote")






#BITWISE OPERATORS
print("Bitwise operators")
"""They include:
AND &
OR |
NOT ~
XOR ^ 
right shift >>
left shit >>
"""
m = 7
n = 6

#and
print(m & m)
print(m & n)

#or
print(m | m)
print(m | n)

#not 
# print(m ~ m)
# print(m ~ n)

#xor
print(m ^ m)
print(m ^ n)

#right shift
print(m >> m)
print(m >> n)

#left shift
print(m << m)
print(m << n)





