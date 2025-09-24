"""Task48:
"""
def print_eng_alphapbet(descending=False):
    if descending:
        for alphabet in range(ord('Z'), ord('A') + 1,-1):
            print(chr(alphabet))
    else:
        for alphabet in range(ord('A'), ord('Z') + 1):
            print(chr(alphabet))


def print_arabic_alph(descending=False):
    if descending == True:
        for alphabet in range(ord('ي'), ord('أ') + 1,-1):
            print(chr(alphabet))
    else:
        for alphabet in range(ord("أ"), ord('ي') + 1):
            print(chr(alphabet))        


if __name__ == "__main__":
    print_arabic_alph()
    print_eng_alphapbet()
    