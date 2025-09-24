"""Task73"""

def get_first_letters_of(string):
    words = string.strip().split(' ')
    letters =[]    

    for word in words:
        letters.append(word[0])

    return " ".join(letters)


def get_abbrevation_of(string):
    prepostions = ['for','in','on','at','the','a','an','at','of']
    words = string.strip().split(' ')
    abbrevations = ""

    for word in words:
        if word not in prepostions:
            abbrevations += word[0].upper() + '.'

    return abbrevations[:-1]


if __name__ == "__main__":
    string = input('Type a string: ')
    is_abbrevation = input('As abbrevation or not? y/n: ').strip().lower() == 'y'

    if is_abbrevation:
        print(get_abbrevation_of(string))
    else:
        print(get_first_letters_of(string))
