"""Task:9"""

if __name__ == '__main__':
    print('----'*25)

    x = int(input('enter x: '))
    y = int(input('enter y: '))
    z = int(input('enter z: '))
    n = int(input("enter n: "))

    permutations = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1)]
    answer = [permutation for permutation in permutations if sum(permutation) != n]
    print(answer)
