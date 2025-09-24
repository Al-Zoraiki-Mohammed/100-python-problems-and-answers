"""Task57"""
def frequency_of(number, digit):
    freq_no = 0
    for dig in (number):
        if dig == digit:
            freq_no +=1
    return freq_no 


def print_frequency_of(number):
    unique_digits = set(number)
    for digit in unique_digits:
        print(f' Frequency of {digit} is {frequency_of(number, digit)}')


if __name__ == "__main__":
    number = input('Type a number: ')
    print_frequency_of(number)
 