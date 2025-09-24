"""Task15"""

def swap_case(s):
    s_m=''
    for letter in s:
        if(letter==letter.upper()):
            s_m += letter.lower()
        else: 
            s_m += letter.upper()
    return s_m

if __name__ == '__main__':
    s = input('Type string with mixed capital and small letters: ')
    print(swap_case(s))
    