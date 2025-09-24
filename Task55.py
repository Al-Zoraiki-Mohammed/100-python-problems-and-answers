"""Task55"""
def sum_of_digits(number):
    sum_of_digits = 0
    for i in range(len(str(number))):
        sum_of_digits += int(number % 10)
        number = int(number /10)
    return sum_of_digits


def print_sum_of_digits(number):
    print(sum_of_digits(number))


if __name__ == "__main__":
    number = int(input('Type a number: '))
    print_sum_of_digits(number)
    