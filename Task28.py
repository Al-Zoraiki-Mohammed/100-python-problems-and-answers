"""Task28"""

def captalize_words(sentence):
    words = sentence.split()
    l = []
    for word in words:
        l.append(word.capitalize())
    return ' '.join(l)


if __name__ == '__main__':
    full_name = input('enter your full name: ')
    print(captalize_words(full_name))
