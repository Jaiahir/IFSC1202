def find_employee(employeeList,empId):
   for employee in employeeList:
       if employee.IDNumber==empId:
           return employeeList.index(employee)
   return -1

class Employee:
   def __init__(self,FirstName,LastName,IDNumber,Wage):
       self.FirstName=FirstName
       self.LastName=LastName
       self.IDNumber=IDNumber
       self.HoursWorked=0
       self.Wage=Wage

   def WeeklyPay(self):
       if self.HoursWorked>=0 and self.HoursWorked<=40:
           return self.Wage*self.HoursWorked
       elif self.HoursWorked>40:
           return (self.Wage*self.HoursWorked) + (1.5*self.Wage)

efile=open("11.02 Employees.txt","r")
employeeList=[]

for empRecord in efile:
   empDetails=empRecord.strip('\n').split(',')
   employee=Employee(empDetails[0],empDetails[1],int(empDetails[2]),float(empDetails[3]))
   employeeList.append(employee)
efile.close()

hfile=open("11.02 Hours.txt","r")
for i in hfile:
   hourInfo=i.strip('\n').split(',')
   index=find_employee(employeeList,float(hourInfo[0]))
   employeeList[index].HoursWorked = float(hourInfo[1])

print("First\tLast\tID\tHours\tHourly\tWeekly")
print("Name\tName\tNumber\tWorked\tWage\tPay")
for employee in employeeList:
   print(employee.FirstName,employee.LastName,employee.IDNumber,employee.HoursWorked,employee.Wage,round(employee.WeeklyPay(),2),sep="\t")
