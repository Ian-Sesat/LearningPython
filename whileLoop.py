noGrades=int(input('how many grades do you have? '))
grades=[]
j=0
while (j<noGrades):
    grade=float(input('Please enter your grades? '))
    grades.append(grade)
    j=j+1
j=0
while(j<noGrades):
    print(grades[j])
    j=j+1
print('Thats all folks')