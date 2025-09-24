"""Task16"""

def split_and_join(line, sep):
    s_l=line.split()
    s_j= f'{sep}'.join(s_l)
    return s_j

if __name__ == '__main__':
    line = input('Type a sentence: ')
    sep = input('Type a separator to use(i.e: - ): ')
    result = split_and_join(line, sep)
    print(result)
