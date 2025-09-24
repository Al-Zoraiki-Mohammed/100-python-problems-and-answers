""" Task: 8"""

if __name__ == '__main__':
    n = int(input('Enter the number of stamps: '))
    s = set()
    for i in range(n):
        s.add(input(f'Enter country {i} name:  '))

    print(len(s))
    