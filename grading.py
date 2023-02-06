"""Create a grading system using the following conditions

SCORE                GRADE
70-100               A
60-69                B
50-59                C
40-49                D
0-39                Fail
"""

sub1 = int(input("Enter the marks of subject 1 :"))
sub2 = int(input("Enter the marks of subject 2 :"))
sub3 = int(input("Enter the marks of subject 3 :"))
sub4 = int(input("Enter the marks of subject 4 :"))
sub5 = int(input("Enter the marks of subject 5 :"))
sub6 = int(input("Enter the marks of subject 6 :"))

score = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6)/6

if (score >= 70 and score <= 100):
    print(" Your grade is A")
elif(score >= 60 and score <= 69):
    print("Your grade is B")    
elif(score >= 50 and score <= 59):
    print("Your grade is C")    
elif(score >= 40 and score <= 49):
    print("Your grade is D")    
elif(score >= 0 and score <= 39):
    print("Your grade is Fail")    
else:
    print("Confirm whether you have entered all the marks")