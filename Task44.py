"""Task44"""
def find_factorial():
    number = read_positive_number()
    factorial = 1 
    for i in range (number):
        factorial *= (number - i)
    print(factorial)


def read_positive_number():
    number = int(input('enter integer number: '))
    while number < 0:
        number = int(input('please enter positive number: '))
    return number

if __name__ == "__main__":
   find_factorial()
   