import pickle
with open('myData2.pkl','rb') as f:
    numStudents=pickle.load(f)
    names=pickle.load(f)
    grades=pickle.load(f)
while(1==1):
    name=input('Please enter the name of the student: ')
    for i in range(0,numStudents,1):
        if (names[i] == name):
            print(str(name)+"'s grade is "+str(grades[i])+'.')
