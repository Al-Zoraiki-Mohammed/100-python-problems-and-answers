"""Task74"""

import string 


def count_letters(text=""):
    words = len(text.strip().split(' '))
    letters = 0
    capital = 0
    small = 0
    punctuations = 0
    spaces = 0

    for letter in text:
        if letter == " ":
            spaces +=1
        elif letter in string.punctuation:
            punctuations +=1
        elif letter == letter.upper(): 
            capital +=1
        else:
            small +=1
    letters = capital + small

    return words, letters, punctuations, spaces, capital, small


if __name__ == "__main__":
    text = input('Type a sting: ')
    words, letters, punctuations, spaces, capital_letters, small_letters = count_letters(text)
    print(f'words = {words}')
    print(f'string length = { len(text)}')
    print(f'Letters small and capital = {letters}')
    print(f'Punctuations = {punctuations}')
    print(f'spaces = {spaces}')
    print(f'Capital Letters = {capital_letters}')
    print(f'small letters = {small_letters}')
    