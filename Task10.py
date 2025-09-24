"""Task10"""
if __name__ == '__main__':
    print('----'*25)
    n = int(input('Enter n: '))
    scores = {int(score) for score in input(f'enter {n} scores: ').strip().split()}
    sorted_scores = sorted(list(scores))
    print(f'The runner-up socore is: {sorted_scores[-2]}')
