import pickle
numStudents=int(input('How many Studens do you have? '))
names=[]
grades=[]
for i in range(0,numStudents,1):
    name=input('Please enter the name of the student: ')
    names.append(name)
    grade=float(input("Please enter the student's grade: "))
    grades.append(grade)
with open('myData2.pkl','wb') as g:
    pickle.dump(numStudents,g)
    pickle.dump(names,g)
    pickle.dump(grades,g)
with open('myData2.pkl','rb') as g:
    a=pickle.load(g)
    b=pickle.load(g)
    c=pickle.load(g)
print(a)
print(b)
print(c)