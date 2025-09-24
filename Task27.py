"""Task27"""

def intial_val(size):
    rows = (size - 1) * 2 + 1 
    cols = (rows - 1)* 2 + 1
    l = [['-' for i in range(cols)] for j in range(rows)] 
    c = 1
    d = 2
    return rows, cols, l, c, d


def draw_first_row(l, i, cols, size):
    l[i][int(cols/2)] = chr(ord('a')+size -1)


def draw_center_row_p1(l, i, j, cols, size):
    for k in range(0,cols,2):
        if k <= int(cols/2):
            l[i][k]= chr(ord('a')+size-1-int(k/2))
        elif k > int(cols/2):
            l[i][k]= l[i][j-k]


def draw_center_row_p2(l, i,j, c):
    l[i][j]= chr(ord(l[i-1][j])-1)
    for k in range(c):
        l[i][j+2*k+2]= chr(ord(l[i][j])+k+1)
        l[i][j-2*k-2]= chr(ord(l[i][j])+k+1)          


def draw_below_row(l, i, d):
    l[i]=l[i-d]


def print_rangoli(size):
    rows, cols, l, c, d = intial_val(size)
    for i in range(rows):
        for j in range(cols):
            if i == 0 :
                draw_first_row(l,i,cols, size)    
            elif i == int(rows/2):
                draw_center_row_p1(l, i, j, cols, size)
            else:
                if j == int(cols/2) and i<(int(rows/2)):
                    draw_center_row_p2(l, i, j, c)
                    c += 1 
        if i > int(rows/2):
            draw_below_row(l, i,d)
            d += 2
                                   
    for item in (l):
        print(''.join(item))


if __name__ == '__main__':
    size = int(input('size: '))
    print_rangoli(size)
