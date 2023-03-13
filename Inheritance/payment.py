"""A program that will calculate the payment of an employee if he or she happens to be either a:-
salary employee,
hourly employee, or 
commission employee

Additional information:- 
Each employee has a health insurance of Kshs 1,500
Allowance for salary employee is not less than 5000
Allowance for hourly employee is not less than 4500
Allowance for commission employee is not less than 4000

"""
#Variables to be used in the program 

idno = int(input("Enter the ID NO of the employee: "))
name = input("Enter the name of the employee: ")
insurance = 1500
monthly_pay = float(input("Enter the monthly pay of the salaried employee kshs: "))
salary_allowance = float(input("Enter the total allowance for the Salaried employee kshs: "))
hourly = float(input("Enter the amount paid per hour kshs: "))
hours = float(input("Enter the total amount of hours worked: "))
hourly_allowance = float(input("Enter the allowance for the hourly employee kshs: "))
commission_rate = int(input("Enter the percentage rate of the commission: "))
total_sales = float(input("Enter the total sales amount kshs: "))
commission_allowance = float(input("Enter allowance given to the commissioned employee kshs: "))



class Employee:
    def __init__(self,idno,name,insurance):
        self.idno = idno
        self.name = name
        self.insurance = insurance

class Salary_Employee(Employee):
    def salarypay(self,salary_allowance,monthly_pay):
        super().__init__(idno,name,insurance)
        salary_total = (monthly_pay + salary_allowance) - insurance
        return salary_total


class Commission_Employee(Employee):
    def commissionpay(self,commission_rate,total_sales,commission_allowance):
        super().__init__(idno,name,insurance)
        commission_pay = (((commission_rate/100) * total_sales) + commission_allowance) - insurance
        return commission_pay


class Hourly_Employee(Employee):
    def hourlypay(self,hourly,hours,hourly_allowance):
        super().__init__(idno,name,insurance)
        hourly_total = ((hourly * hours) + hourly_allowance) - insurance
        return hourly_total


S = Salary_Employee(insurance,salary_allowance,monthly_pay)

C = Commission_Employee(commission_rate,total_sales,commission_allowance)

H = Hourly_Employee(hourly,hours,hourly_allowance)


print("If user was a Salaried employee he earns kshs: ", S.salarypay(salary_allowance,monthly_pay))

print("If user was a Commissioned employee he earns kshs: ", C.commissionpay(commission_rate,total_sales,
                                                                                     commission_allowance))

print("If user was an Hourly employee he earns kshs: ", H.hourlypay(hourly,hours,hourly_allowance))
 