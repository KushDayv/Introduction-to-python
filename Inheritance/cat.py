"""  
Create a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and 
methods like calculate_emp_salary,  and employee_details. 

(i) Use 'employee_details' method to print the details of an employee.

Sample Employee Data:
"James", "ZU22", 50000, "ACCOUNTING"
"Natalia", "ZU19", 45000, "IT"

Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, 
which is the number of hours worked by the employee.
 If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. 
 Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))"""

#Program to calculate the amount earned by an employee 

emp_id = int(input("Enter the employee id: "))
emp_name = input("Enter the employee name: ")
emp_salary = float(input("Enter the employee salary: "))
emp_department = input("Enter the employee department: ")
hours_worked = int(input("Enter the hours worked: "))

overtime = hours_worked - 50
Overtime_amount = (overtime * (emp_salary / 50))
Total_amount = emp_salary + Overtime_amount



if (hours_worked > 50):
    print("Your over time amount is: ",Overtime_amount)
else:
    print("No overtime amount!!")
    


class Employee:
    def employee_details(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id = emp_id
        self.name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        return emp_id,emp_name,emp_salary,emp_department
        


    def calculate_emp_salary(self,hours_worked):
        super().__init__()
        self.hours_worked = hours_worked
        return Overtime_amount,Total_amount
    

S = Employee()

print("The employee details are: ", S.employee_details(emp_id,emp_name,emp_salary,emp_department))
print("The amount earned is: ", S.calculate_emp_salary(hours_worked))
