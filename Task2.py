''' Task2: in the Tasks.docx file'''

def check_num(num=0):
    #Read the number
    n = int(input('input number n: ').strip())

    # The first condition when n is Weird.
    if (n%2!=0) or ((n%2==0) and (n>=6) and (n<=20)):
        print('Weird')

    # The second condition when n is Not Weird.
    elif ((n%2==0) and (n>=2) and (n<=5) or ((n%2==0)and(n>20))):
        print('Not Weird')

if __name__ == '__main__':
    check_num()
