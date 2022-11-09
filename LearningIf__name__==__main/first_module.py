
#print (__name__)
def myName(name):
    print('My name is {}'.format(name))
def main():
    print('We are running the first module from: {}'.format(__name__))
if __name__ =='__main__':
    __name__='the file itself'
    main()