noGrades=int(input('How many grades do you have? '))
grades=[]
for i in range(0,noGrades,1):
    grade=float(input('Please enter your grade: '))
    grades.append(grade)
    print(grades)
print('Your grades are: ')
for i in range(0,noGrades,1):
    print(grades[i])
print('Thats all folks')
