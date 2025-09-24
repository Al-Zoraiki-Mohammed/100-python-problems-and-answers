"""Task64"""

def read_elemnts():
    array = []
    N = int(input(("Type how many numbers to store? : ")))
    for i in range(N):
        element = int(input(f'Type elment [{i}]: '))
        array.append(element)
    return array


def check_frequency(array):    
    element = int(input('Type elemnt to check: '))
    frequency = 0
    for elm in array:
        if elm == element:
            frequency +=1
    return element, frequency


def print_array(array):
    print(f"original array: ", end ="")
    for elm in array:
        print(elm, end = " ")


if __name__ == "__main__":
    array = read_elemnts()
    element, frequency = check_frequency(array)
    print_array(array)
    print(f'\n {element} is repeated {frequency} times.')
    