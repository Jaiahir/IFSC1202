class Employee:
    def __init__(self,fname,lname,idn,hworked,wage):
        self.FirstName = fname
        self.LastName = lname
        self.IDNumber = idn
        self.HoursWorked = hworked
        self.Wage = wage

    def WeeklyPay(self):
        if self.HoursWorked <= 40:
            return self.HoursWorked * self.Wage
        return (40*self.Wage) + ((self.HoursWorked-40)*1.5 * self.Wage)

print("   First    Last      ID   Hours  Hourly  Weekly\n    Name    Name  Number  Worked    Wage     Pay")
file = open("10.06 Payroll.txt", "r")

for line in file.readlines():
    x = line.split(',')
    x = Employee(x[0].strip(),x[1].strip(),int(x[2]),float(x[3]),float(x[4]))
    print("%8s%8s%8d%8.2f%8.2f%8.2f"%(x.FirstName,x.LastName,x.IDNumber,x.HoursWorked,x.Wage,x.WeeklyPay()))

file.close()