"""Task63"""
import random
import string

def generate_keys(keys_no=1, word_no=4, word_length=4, separtor='-'):
    for i in range(keys_no):
        print(f'key [{i+1}]: {generate_key(word_no=4, word_length=4, separtor="-")}')


def generate_key(word_no=4, word_length=4, separtor='-'):
    key = ""
    for i in range(word_no):
        if i == word_no -  1:
            key += generate_words(word_length=4)
        else:
            key += generate_words(word_length=4) + separtor
    return key 


def generate_words(word_length=4):
    word = ""
    for i in range(word_length):
        word += random.choice(string.ascii_uppercase)
    return word
    

if __name__ =="__main__":
    keys_no = int(input('Type how manys to generate?: '))
    generate_keys(keys_no)
    