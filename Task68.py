"""Task68"""
def input_validated_number():
    """Validation using try except"""
    while True:
        number = input('type a number: ')
        try:
            number = int(number)
            return number
        except ValueError:
            print(f'{number} is not int or float! ')


def validate_number(num_str):
    """Validation using isdigit() method of string object"""
    while True:
        if num_str.isdigit():
            return int(num_str)
        else:
            num_str = input('type integer number: ')


if __name__ == "__main__":
    number = input_validated_number()
    print(f'you entered correct number: {number}')
    #---------- Alternative solution --------
    num_str = input('type a number: ')
    num = validate_number(num_str)
    print(f'num = {num}')