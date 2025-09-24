"""Task43"""
def check_age(lower_bound = 18, upper_bound = 45):
    age = int(input(f'Type your age, it should be between {lower_bound} and {upper_bound}: '))
    while age < lower_bound or age > upper_bound:
        age = int(input(f'Invalid age, please type valid age: '))
    print(f'{age} is valid age :)')


if __name__ == "__main__":
    check_age()
