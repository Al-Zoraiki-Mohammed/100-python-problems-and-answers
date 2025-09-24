"""Task42"""

def find_max():
    numbers = int(input('how many numbers to compare? : '))
    max = int(input('Type number 1: '))
    for i in range(1,numbers):
        number = int(input(f'Type number {i + 1}: '))
        if number > max:
            max = number
    print(f' The maximum number is: {max}')


if __name__ == '__main__':
    find_max()
