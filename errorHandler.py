def writing_file():
    with open('numbers.txt','w') as f:
        f.write("100\n70\n30\nabc\n20\n10")

def reading_file_and_getting_numbers():
    with open('numbers.txt','r') as f:
        lines=f.read()
        lines=lines.split('\n')
        numbers=[]
        for line in lines:
            try:
                numbers.append(int(line))
            except Exception as e:
                exception_checker(e,line)
    return numbers

def exception_checker(e,l):
    exceptionName= type(e).__name__
    print('An unexpected error occured while adding {} to the list: {}'.format(l,exceptionName))
def results_writer(sum):
    with open('results.txt','w') as f:
        result='The sum of your integers in your text file is: {}'.format(sum)
        f.write(result)

def main():
    writing_file()
    numbers=reading_file_and_getting_numbers()
    total=sum(numbers)
    if len(numbers)>0:
        print('The sum of valid numbers in the text is: {}'.format(sum(numbers)))
    else:
        print('No valid number was present in the text')
    results_writer(total)
    
if __name__=='__main__':
    main()

        
