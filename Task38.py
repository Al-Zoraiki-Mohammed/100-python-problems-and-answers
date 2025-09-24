"""Task38"""
def check_number(number):
    if number % 2 == 0:
        print(f'The number {number} is even :)')
    else: 
        print(f'The number {number} is odd :)')

if __name__ == "__main__":
    number = int(input('Type a number: '))
    check_number(number)
