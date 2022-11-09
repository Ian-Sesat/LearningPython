#Learning the use of a property decorator, a getter, a setter and a deleter

class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print('Deleted {} {} from the system'.format(self.first,self.last))
        self.first=None
        self.last=None
    
emp1=Employee('Ian','Sesat')
emp1.first='Taji'
print(emp1.fullname)

emp1.fullname='Taji Kibet'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
print(emp1.email)
print(emp1.fullname)