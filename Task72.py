"""1,1,2,3,5,8,13,21,34,… n."""


def generate_fib_recrussion(previous, last, limit):
    """Unrecommended solution using recurssion"""
    if last <= limit:
        print(last)
        generate_fib_recrussion(last , previous+last, limit)


def genterate_fib_loop(previous, last, limit):
    """Alternative recommened solution using while loop"""
    while last < limit:
        temp = last
        last +=previous
        previous = temp
        print(last)


if __name__ =="__main__":
    limit = int(input('Type postive interger n: '))
    generate_fib_recrussion(0, 1, limit)
    print('\t------ using loop ---------')
    genterate_fib_loop(0,1,limit)
    