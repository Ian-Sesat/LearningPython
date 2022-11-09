class Student:
    #Initializing our class:
    def __init__(self,first,last,mark1,mark2,mark3):
        #Working with our attributes ie the data of the class......
        self.fname=first
        self.lname=last
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    #Initialzizing our methods
    def average(self):
        return float(self.mark1+self.mark2+self.mark3)/3
    def fullname(self):
        return self.fname+' '+self.lname

student1=Student('Ian','Sesat',96,98,97)#our first instance
student2=Student('Lionel','Ronaldo',87,86,85)#our second instance

print(student1.fullname())
print('This student has an average mark of ',student1.average())