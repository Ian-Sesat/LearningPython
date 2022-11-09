noGrades=int(input('How many grades do you have? '))
grades=[]
bucket=0
highestNo=0
lowGrade=100
for i in range(0,noGrades,1):
    grade=float(input('What is your grade? '))
    grades.append(grade)
for i in range(0,noGrades,1):
    print(grades[i])
for i in range(0,noGrades,1):
    bucket=bucket+grades[i]
average=bucket/noGrades
print('Your average is',average)
for i in range(0,noGrades,1):
    if (grades[i]>highestNo):
        highestNo=grades[i]
print('Your highest grade is',highestNo)
for i in range(0,noGrades,1):
    if(grades[i]<lowGrade):
        lowGrade=grades[i]
print('Your lowest grade is',lowGrade)
for i in range(0,noGrades-1,1):
    for i in range(0,noGrades-1,1):
        if(grades[i]<grades[i+1]):
            swap=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=swap
print('Your sorted grades are:')
for i in range(0,noGrades,1):
    print(grades[i])
