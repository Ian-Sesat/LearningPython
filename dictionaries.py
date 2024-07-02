dict={'China':143,'India':136,'USA':32,'Pakistan':21}

def add():
    country=input('Which country do you want to add? ')
    if country in dict:
        print('Country already exists') 
    else:
        population=input('Enter the population of '+country+' : ')
        dict[country]=population
    print(dict)
def print_all():
    for c,p in dict.items():
        print(c+'==>'+str(p))

def remove():
        print(dict)
        country=input('Which country do you want to remove? ')
        if country in dict:
            del dict[country]
            print('Country removed successfully') 
            print(dict)
        else:
            print("Country's data does not exist")
def query():
    country=input("Which country's population do you want to know? ")
    if country in dict:
        print("{} has a population of {} people".format(country,str(dict[country])))
    else:
        print('Country is not present')

def invalid():
    print('Invalid input')

def main():
    need=input('What action do you want to do: print, add, remove or query? ')  
    if need.lower()=='add':
        add()
    if need.lower()=='print':
        print_all()
    if need.lower()=='query':
        query()
    if need.lower()=='remove':
        remove()
    if need.lower()=='invalid':
        invalid()
if __name__ == '__main__':
    main()

