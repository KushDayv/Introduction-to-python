"""The function will calculate the compound interest of so as to get the 
final amount at the end of a given period of time
A = P(1 + {r/n})^{nt}
where :
A = final amount 
P = Initial principal balance
r = intrest rate
n = number of times intrest is compounded per year
t = time in years
"""

#Function to calculate the compound intrest
from math import pow

Principal = int(input("Enter the Principal amount : "))
rate = int(input("Enter the rate per year as a percentage : % "))
no = float(input("Enter the number of times the intrest is compunded : "))
time = int(input("Enter the time total time in years : "))


def compound_intrest(Principal,rate,no,time):
    A = Principal * pow((1 + (rate/100)/no),no*time)
    CI = A - Principal
    return CI

print("The compound intrest (CI) is : ", compound_intrest(Principal,rate,no,time))
