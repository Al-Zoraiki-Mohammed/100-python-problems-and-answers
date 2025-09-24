"""Task62.py"""
import random
import string


def random_word():
    word = random.choice(string.ascii_uppercase)
    word += random.choice(string.ascii_lowercase)
    word += random.choice(string.punctuation)
    word += random.choice(string.digits)
    return word


if __name__ == "__main__":
    print(random_word())
    