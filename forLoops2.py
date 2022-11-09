numGrades=int(input('How many grades do you have? '))
grades=[]
total=0
for n in range(0,numGrades,1):
    grade=float(input('Please enter your grades: '))
    grades.append(grade)
print('Your grades are: ')
for n in range(0,numGrades,1):
    print(grades[n])
for n in range(0,numGrades,1):
    total=total+grades[n]
average=total/numGrades
print('Your average is',average)



    
