"""Task23"""

def print_door(n,m):
    d=0
    for i in range(n):
        if i < int(n/2):
            print('-'*(int(m/2-(2*i+1))-i)+ '.|.'*int((2*i+1))+  '-'*(int(m/2-(2*i+1)-i)))
        elif i== int(n/2):
            print('-'*int((m-len('WELCOME'))/2) + 'WELCOME' + '-'*int((m-len('WELCOME'))/2) )
        elif i > n/2:
            d += 2
            print('-'*int((m-((n-d)*3))/2) + '.|.'*int(n-d) +  '-'*int((m-((n-d)*3))/2))


def print_door2(n,m):
    '''alternative solution'''
    row = (n-1)
    for i in range(0,row+1):
        character = ".|."
        if(i%2 != 0):
            character = character*i
            print(character.center(m,"-"))
        elif(i == row):
            print("welcome".upper().center(m,"-"))
        else:
            continue
    for i in range(row,0,-1):
        character = ".|."
        if(i%2 != 0):
            character = character*i
            print(character.center(m,"-"))
        else:
            continue
   
    
if __name__ == '__main__':

    n,m =[int(i) for i in (input('input n,m (e.g 3 9 ): ').strip().split())]
    print_door(n,m)
    print('\nAlternative solution: \n')
    print_door2(n,m)
