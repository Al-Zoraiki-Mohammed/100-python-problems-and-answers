"""Task65"""
import random


def fill_array(size = 100):
    array = []
    for i in range(size):
        array.append(random.randint(1,size))
    return array


def print_array(array):
    print('array elements: ', end='')
    for element in array:
        print(element, end=" ")


if __name__ == "__main__":
    size = int(input('Type the size of the array: '))
    array = fill_array(size)
    print_array(array)
    