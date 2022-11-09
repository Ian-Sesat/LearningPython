class Employee:
    raise_rate=1.04
    def  __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=self.first+'.'+self.last+'@gmail.com'
        self.pay=pay
    def fullname(self):
        return self.first+' '+self.last
    def raise_pay(self):
        self.pay=int(self.pay*self.raise_rate)
        return self.pay
#Creating our subclasses with inheritance properties:
class Developer(Employee):
    raise_rate=1.08
    def __init__(self,first,last,pay,progLanguage):
        super().__init__(first,last,pay)
        self.progLanguage=progLanguage
#Creating another subclass called manager that inherits the characteristics of the Employee class too
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    
    def add_Employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_Employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        print('The Manager '+self.fullname()+' supervises the following people:' )
        i=0
        for emp in self.employees:
            i+=1
            print(i,emp.fullname())

    
emp1=Employee('Ian','Sesat',500000)
emp2=Employee('Joe','Ruto',500000)
dev1=Developer('Mbaga','Hamburgers',600000,'Assembly')
#print(emp1.pay)
#emp1.raise_pay()
#print(emp1.pay)
#dev1=Developer('Ian','Sesat',500000,'Python')
#print(emp1.email)
#print(help(Manager))
automationManager=Manager('Schecks','Kapienga',100000)
automationManager.add_Employee(emp1)
automationManager.add_Employee(dev1)
automationManager.add_Employee(emp2)
automationManager.remove_Employee(emp2)
automationManager.print_emps()