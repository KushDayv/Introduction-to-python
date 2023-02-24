"""A a grading system using the following conditions

SCORE                GRADE
70-100               A
60-69                B
50-59                C
40-49                D
0-39                 E(Fail)

For 39% and below one is required to sit for a supplementary
"""


unit1 = int(input("Enter the marks of unit 1 :"))
unit2 = int(input("Enter the marks of unit 2 :"))
unit3 = int(input("Enter the marks of unit 3 :"))
unit4 = int(input("Enter the marks of unit 4 :"))
unit5 = int(input("Enter the marks of unit 5 :"))
unit6 = int(input("Enter the marks of unit 6 :"))


if unit1 < 0 or unit2 < 0 or unit3 < 0 or unit4 < 0 or unit5 < 0 or unit6 < 0 :
    raise ValueError("Negative values are not allowed")
if unit1 > 100 or unit2 > 100 or unit3 > 100 or unit4 > 100 or unit5 > 100 or unit6 > 100:
    raise ValueError("Marks cannot exceed 100%")


score = (unit1 + unit2 + unit3 + unit4 + unit5 + unit6)/6


if (score >= 70 and score <= 100):
    print(" Your grade is A")
elif(score >= 60 and score <= 69):
    print("Your grade is B")    
elif(score >= 50 and score <= 59):
    print("Your grade is C")    
elif(score >= 40 and score <= 49):
    print("Your grade is D")    
elif(score >= 0 and score <= 39):
    print("Your grade is Fail !! You are required to sit for a Supplementary exam")    
else:
    print("Confirm whether you have entered all the marks")