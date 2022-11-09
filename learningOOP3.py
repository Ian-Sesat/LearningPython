import datetime
class Employee:
    numberOfEmployees=0
    raise_rate=1.05
    def __init__ (self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def fullName(self):
        return self.first+' '+self.last
    #Making of a class method
    @classmethod
    def set_raise_rate(cls,raise_rate):
        cls.raise_rate=raise_rate
        return cls.raise_rate
    #Using a class method as an alternative constructor:
    @classmethod
    def  split_string(cls,statement):
        first,last,pay=statement.split('-')
        return cls(first,last,pay)
    #Using static methods to determine if the given date and time is a weekday:
    #A static method does not need a self or a cls argument to be passed to it
    @staticmethod
    def is_workday(data):
        if data.weekday()== 5 or data.weekday()==6:
            return False
        else:
            return True
#emp1=Employee('Steve','Jobs',10000)
#print(emp1.fullName())
#print(Employee.set_raise_rate(1.05))
emp_1='Mark-Ek-20000'
emp_2='Jeff-Musk-10000'
emp1=Employee.split_string(emp_1)
print(emp1.fullName())
myData=datetime.date(2022,8,7)
print(Employee.is_workday(myData))


