class Employee:
    def __init__(self,id,occupation):
        self.id=id
        self.occupation=occupation
    def role(self):
        print('Employee{} is a {} in the company'.format(self.id,self.occupation))
def del_ID(employee,employeeNum):
    try:
        del employee.id
        print('{} id attribute has been sucessfully deleted'.format('Employee'+employeeNum))
    except Exception as e:
        print('{} id does not exist'.format('Employee'+employeeNum))
        
def del_Object(employee,employeeNum):
    try:
        del employee
        print('{} object has been sucessfully deleted'.format('Employee'+employeeNum))
    except:
        print('{} object does not exist'.format('Employee'+employeeNum))

def main():
    employee1=Employee(1,'Coder')
    employee1.role()
    employee2=Employee(2,'HR')
    employee2.role()
    employee3=Employee(3,'Manager')
    employee3.role()
    #Deleting employee1 ID :
    del_ID(employee1,'1')
    #Deleting employee1 object:
    del_Object(employee1,'1')
    try:
        employee1.role()
    except:
        print('{} object has already been deleted'.format('Employee1'))

if __name__ == "__main__":
    main()
    