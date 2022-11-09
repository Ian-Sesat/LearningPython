numGrades=int(input('How many grades do you have?'))
grades=[]
sumValue=0
greatValue=0
smallValue=100
for i in range(0,numGrades,1):
   grade=float(input('What is your grade?'))
   grades.append(grade)
print('Your grades are:')
for i in range(0,numGrades,1):
    print(grades[i])
for i in range(0,numGrades,1):
    sumValue=sumValue+grades[i]
averageValue=sumValue/numGrades
print('Your average value is',averageValue)
for i in range(0,numGrades,1):
    if (grades[i]>greatValue):
        greatValue=grades[i]
print('Your greatest value is',greatValue)
for i in range(0,numGrades,1):
    if(grades[i]<smallValue):
        smallValue=grades[i]
print('Your smallest Value is',smallValue)