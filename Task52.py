
"""Task52"""
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


def print_result(is_perfect, number):
    if is_perfect:
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")


if __name__ == "__main__":
    number = input_positive_number()
    print_result(check_perfect(number), number)
    