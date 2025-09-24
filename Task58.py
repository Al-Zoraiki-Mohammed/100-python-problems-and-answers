"""Task58"""

def reverse_number(number):
    return number[::-1]


def is_palindrome(number):
    return (number == reverse_number(number))


if __name__ == "__main__":
    number = input('Type a number: ')
    if is_palindrome(number):
        print(f'{number} is palindrome')
    else:
        print(f'{number} is not palindrome')

  