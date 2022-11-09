#This code is about learning of the class variables
class Employee:
    #Our class variables appear before the initialization of the class by the init method
    raiseRate=1.04
    numberOfEmployees=0
    def __init__ (self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee.numberOfEmployees+=1
    def increaseWages(self):
        self.pay=int(self.pay*self.raiseRate)

emp1=Employee('Elon','Trump',5000)
emp2=Employee('Donald','Musk',10000)
print(Employee.numberOfEmployees)
print(emp1.pay)
emp1.increaseWages()
print(emp1.pay)
emp2.raiseRate=1.1
emp2.increaseWages()
print(emp2.pay)