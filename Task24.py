'''This code converts number from one system to another from scratch,
 without using built-in functions (bin(),hex(),etc.) which have been done
in script Task24_v2
'''

def to_octal(decimal):
    octal =''
    if decimal <= 7:
            octal = decimal
    else:
        d = ''
        while (decimal > 0):
            d += str(to_octal(decimal % 8))
            decimal =int(decimal/8) 
        octal= ''.join(reversed(d))
    return octal


def to_hexa(decimal):
    hexa =''
    if decimal <= 9:
        hexa = decimal
    elif decimal in (10,11,12,13,14,15):
        if decimal == 10 : hexa = 'A'
        elif decimal == 11 : hexa = 'B'
        elif decimal == 12 : hexa = 'C'
        elif decimal == 13 : hexa = 'D'
        elif decimal == 14 : hexa = 'E'
        elif decimal == 15 : hexa = 'F'
    elif decimal >= 16:
        d = ''
        while (decimal > 0):
            d += str(to_hexa(decimal % 16))
            decimal = int(decimal/16) 
        hexa = ''.join(reversed(d))
    return hexa


def to_binary(decimal):
    binary = ''
    while (decimal>0):
        binary += str(decimal % 2)
        decimal= int(decimal /2)
    binary = ''.join(reversed(binary))
    return binary


def print_formatted(number):
    padding = len(bin(number)) - 2
    for i in range(number):
        decimal = i+1
        octal = to_octal(decimal)
        hexa = to_hexa(decimal)
        binary = to_binary(decimal)
        
        print(f'{decimal:>{padding}}', f'{octal:>{padding}}', f'{hexa:>{padding}}', f'{binary:>{padding}}')


if __name__ == '__main__':
    print(' New Run :) '.center(100,'-'))
    n = int(input('Enter number  n: '))
    print_formatted(n)
