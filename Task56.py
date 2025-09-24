"""Task56"""
def read_number_digit():
    number = input('Type a number: ')
    digit = input ('Type a digit: ')
    while( digit not in number):
       digit = input (f'{digit} not in { number}. Type another digit: ')
    return number, digit
 

def frequency_of(number, digit):
    freq_no = 0
    for dig in (number):
        if dig == digit:
            freq_no +=1
    return freq_no
def print_frequency_of(number, digit):
    print(f' Frequency of {digit} is {frequency_of(number, digit)}')


if __name__ == "__main__":
    number, digit = read_number_digit()
    print_frequency_of(number, digit)
    