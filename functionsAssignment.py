def inputGrades(nm):
    grades=[]
    for i in range(0,nm,1):
        grade=float(input('Please enter your grades: '))
        grades.append(grade)
    return grades

def printGrades(nm,x):
    for i in range(0,nm,1):
        print(x[i])

def averageGrades(nm,x):
    previous=0.0
    for i in range(0,nm,1):
        current=previous+x[i]
        previous=current
        avge=current/nm
    return avge
def highestGrade(nm,x):
    highest=0.0
    for i in range(0,nm,1):
        if(x[i]>highest):
            highest=x[i]
    return highest  

def lowestGrade(nm,x):
    lowest=100
    for i in range(0,nm,1):
        if(x[i]<lowest):
            lowest=x[i]    
    return lowest
numGrades=int(input('How many grades do you have? '))
myGrades=inputGrades(numGrades)
print('Your grades are: ')
printGrades(numGrades,myGrades)
avge=averageGrades(numGrades,myGrades)
print('Your average grade is ', avge)
highestNo=highestGrade(numGrades,myGrades)
print('Your highest grade is ', highestNo)
lowestNo=lowestGrade(numGrades,myGrades)
print('Your lowest grade is ', lowestNo)



