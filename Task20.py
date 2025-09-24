"""Task20"""


def check_string(s):
    d = {'alnum':False,'alpha':False,'digit':False,'lower':False,'upper':False}
    for c in s:
        d['alnum'] = c.isalnum()
        d['alpha'] = c.isalpha() or d['alpha']
        d['digit'] = c.isdigit() or d['digit']
        d['lower'] = c.islower() or d['lower']
        d['upper'] = c.isupper() or d['upper']
    return d

if __name__ == '__main__':
    s = input('Enter String: ')
    d = check_string(s)
    for key,value in d.items():
        print(value)

