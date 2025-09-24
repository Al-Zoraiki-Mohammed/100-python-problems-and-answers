"""Task17"""

def print_full_name(first, last):
    line =f'Hello {first} {last}! You just delved into python.'
    print(line) 

if __name__ == '__main__':
    first_name = input('Type yr first name: ')
    last_name = input('Type yr last name: ')
    print_full_name(first_name, last_name)
    