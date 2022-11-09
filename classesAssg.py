class students:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def inputGrades(self,ng):
        self.ng=ng
        self.grades=[]
        for i in range(0,ng,1):
            self.grade=float(input('Please enter your grade: '))
            self.grades.append(self.grade)
        return self.grades
    def displayGrades(self):
        print('')
        for i in range(0,self.ng,1):
            print(self.first+"'s grades are:",self.grades[i])
    def averageGrade(self):
        sum=0
        for i in range(0,self.ng,1):
            sum=sum+self.grades[i]
        self.average=sum/self.ng
        print('')
        print(self.first+"'s average is:",self.average)
    def highLow(self):
        high=0
        low=100
        print('')
        for i in range(0,self.ng,1):
            if self.grades[i]>high:
                high=self.grades[i]
            if self.grades[i]<low:
                low=self.grades[i]
        print(self.first+"'s lowest grade is", low)
        print(self.first+"'s highest grade is",high)


print('Ian Sesat students report card')      
student1=students('Ian','Sesat')
student1.inputGrades(4)
student1.displayGrades()
student1.averageGrade()
student1.highLow()
print('')
print('Nelly Ruby students report card')
student2=students('Nely','Ruby')
student2.inputGrades(6)
student2.displayGrades()
student2.averageGrade()
student2.highLow()