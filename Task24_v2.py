"""Task24"""

def print_formatted(n):
    padding = len(bin(n))-2
    for i in range (n):
        decimal = i+1
        hexa = hex(decimal).upper()[2:]
        octal = oct(decimal)[2:]
        binary = bin(decimal)[2:]

        print(f'{decimal:>{padding}}',
               f'{octal:>{padding}}', 
               f'{hexa:>{padding}}', 
               f'{binary:>{padding}}')

if __name__ == '__main__':
    n = int(input('Type the maximum value to print (int): '))
    print_formatted(n)
