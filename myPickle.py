import pickle
fruits=['bananas','oranges','tomatoes']
x=9
y=8
colors=['white','red']
with open ('myData.pkl','wb')as f:
    pickle.dump(fruits,f)
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(colors,f)
with open('myData.pkl','rb') as f:
    a=pickle.load(f)
    b=pickle.load(f)
    c=pickle.load(f)
    d=pickle.load(f)
print(a)
print(b)
print(c)
print(d)