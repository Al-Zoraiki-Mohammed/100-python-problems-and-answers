"""Task51"""
def input_positive_number():
    n = int(input("Enter a positive number: "))
    while n <=0:
        n = int(input("Enter a positive number: "))
    return n


def check_prime(j):
    is_prime = True
    for i in  range(3, int(j/2) +1):
        if j % i == 0:
            is_prime = False
            break
    return is_prime and j !=4


def print_prime_numbers(n):
    for j in range (1, n+1):
        if check_prime(j) == True:
            print(f'{j} is a prime number')
        else:
            print(f'{j} is not a prime number')

if __name__ == "__main__":
    n = input_positive_number()
    print_prime_numbers(n)
    