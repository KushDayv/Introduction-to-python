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
print(a%b)


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





