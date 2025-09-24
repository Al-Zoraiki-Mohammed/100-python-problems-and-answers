"""Task37"""

def calc_happiness(array, A, B):
    ''''''
    happiness = 0
    for item in array:
        if item in A:
            happiness +=1
        elif item in B:
            happiness -=1
    print(happiness)


if __name__ =='__main__':
    n, m = input('Type n and m values separted with space: ').split()
    n, m = int(n), int(m)
    array = [int(i) for i in (input(f'Type {n} numbers separated with space: ').split())]
    A = set([int(i) for i in (input(f'Type {m} elements for A: ').split())])
    B= set([int(i) for i in (input(f'Type {m} elements for B: ').split())])
    calc_happiness(array, A, B)

    '''
    Sample Input:
    3 2
    1 5 3
    3 1
    5 7
    sample output:
    1
    '''
    