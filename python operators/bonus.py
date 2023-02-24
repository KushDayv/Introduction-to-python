"""A company decided to give bonus to employee according to the following 
criteria :
Time period of service             Bonus

More than 10 years                   10%
>=6 years and <=10 years             8%
Less than 6 years                    5%

Ask user for their salary and years of service and print the net bonus amount"""

salary = float(input("Enter your salary :"))
years_of_service = float(input("Enter your years of service"))

if (years_of_service > 10 ):
    print("You have been awarded a net bonus of :",(10/100)*salary)
elif(years_of_service >= 6 and years_of_service <= 10):
    print("You have been awarded a bonus of ",(8/100)*salary)
elif(years_of_service < 6 ):
    print("You hav been awarded a bonus of ",(5/100)*salary)
    