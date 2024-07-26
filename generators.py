def square():
    a=1
    while True:
        yield a**2
        a+=1

for f in square():
    if f > 100:
        break
    print(f)