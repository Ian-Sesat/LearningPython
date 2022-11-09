#Learning about special(magic/dunder)Methods
#Magic methods have 4 underscores eg def __init__ which has 4 underscores
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=self.first+self.last+'@gmail.com'
    def fullname(self):
        return self.first+' '+self.last
    #Making the magic method __repr__
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    #Making the magic method __str__
    def __str__(self):
        return self.fullname()+'-'+self.email
    #Making the magic method __add__
    def __add__(self,other):
        return self.pay+other.pay
    #Making the magic method __len__
    def __len__(self):
        return len(self.fullname())-1
emp1=Employee('Ian','Sesat',500000)
emp2=Employee('Freedom','Fighter',1000000)
print(emp1.fullname())
#print(int.__add__(1,12))
#print(str.__add__('a','b'))
print(emp1.__add__(emp2))
print(emp2.__len__())
#print(help(emp1))
