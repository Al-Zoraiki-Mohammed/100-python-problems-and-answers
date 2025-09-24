"""Task26"""

def solution(A):
    l = list(A)
    L = []
    for i in range(len(l)):
        L.append(''.join(l[0:i]+l[i+1:])) 
    return min(L)

if __name__ == '__main__':
    print(solution('codility'))
