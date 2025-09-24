'''Task19'''

def count_substring(string, sub_string):
    c = 0
    if sub_string in string:
        for i in range(len(string)):
            if sub_string in string[i:(i+len(sub_string))]:
                c+=1
    return c

if __name__ == '__main__':
    string = input('enter string: ').strip()
    sub_string = input('enter substring: ').strip()
    count = count_substring(string, sub_string)
    print(count)
    