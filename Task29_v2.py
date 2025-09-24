"""Task29_v2"""

def minion_game(word):
    Kevin_scores = 0
    Stuart_scores = 0
    vowels = 'AEOUI'
    length = len(word)

    for i in range (len(word)): 
        if  word[i] in vowels:
            Kevin_scores += length - i
        else:
            Stuart_scores += length - i 

    if Stuart_scores > Kevin_scores:
        print(f'Stuart {Stuart_scores}')
    elif Stuart_scores < Kevin_scores:
        print(f'Kevin {Kevin_scores}')
    else:
        print('Draw')  


if __name__ == '__main__':
    word = input('input a word: ')
    minion_game(word)
