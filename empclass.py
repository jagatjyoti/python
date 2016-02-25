#!/usr/bin/python


class Employee:

  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def displayCount(self):
    print "Total number of employee is %d"  % Employee.empCount

  def displayEmployee(self):
    print "Name :", self.name,  ", Salary: ", self.salary

"This would create record of first employee"
emp1 = Employee("Ramesh", 5000)
"This would create record of second employee"
emp2 = Employee("Sruti", 8000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total no. of employee: %d"  % Employee.empCount
