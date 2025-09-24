
"""Task53"""
def input_positive_number():
    n = int(input("Enter a positive number: "))
    while n <=0:
        n = int(input("Enter a positive number: "))
    return n


def get_divisors(number):
    divisors = list()
    for i in range(1, number):
        if number % i ==0:
            divisors.append(i)
    return divisors


def check_perfect(number):
    divisors = get_divisors(number)
    return sum(divisors) == number


def print_perfect_numbers(number):
    for i in range(1, number):
        if check_perfect(i) == True:
            print(i)


if __name__ == "__main__":
    number = input_positive_number()
    print_perfect_numbers(number)
    
    