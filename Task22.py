print('----'*10+'New Run :)'+'----'*10)
def wrap(string, max_width):
    r_txt=string[0:max_width]+'\n'
    c=0
    for i in range(len(string)):
        c +=1
        if c==max_width:
            r_txt += (string[i+1:i+max_width+1] + '\n')
            c=0

    return r_txt

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)