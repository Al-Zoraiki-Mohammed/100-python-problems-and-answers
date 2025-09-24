"""Task46"""
def check_prime(number):
    is_prime = True
    for i in range(2, int(number/2)+1):
        if number % (i) ==0:
            is_prime = False
            break
    if is_prime or number == 2:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')


if __name__ == "__main__":
    number = int( input('Type a number: '))
    while number <=0:
        number = int( input('Type a number > 0: '))
    check_prime(number)
    