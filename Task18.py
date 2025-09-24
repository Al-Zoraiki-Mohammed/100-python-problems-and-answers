"""Task18"""

def mutate_string(string, idx, char):
    s = list(string)
    s[int(idx)] = char
    updated_s = ''.join(s)   
    return updated_s


def mutate_using_slicing(s, idx, char):
    updated_s = s[:int(idx)] + char + s[int(idx)+1:]
    return updated_s


if __name__ == '__main__':
    s = input('Type string: ')
    i, c = input('Type the index of the letter to be modifed, followed by the new letter: ').split()
    updated_s = mutate_string(s, i, c)
    print(updated_s)
    updated_s = mutate_using_slicing(s,i,c)
    print(updated_s)
