num=float(input('Please enter your number: '))
rem=num%2
if(num>0 and rem==0):
    print('Your number is an even positive number')
if(num>0 and rem==1):
    print('Your number is an odd positive number')
if(num<0 and rem==0):
    print('Your number is an even negative number')
if(num<0 and rem==1):
    print('Your number is an odd negative number')
if(num==0):
    print('Your number is 0')