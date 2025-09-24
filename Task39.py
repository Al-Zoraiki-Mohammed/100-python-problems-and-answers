"""Task39"""
def check_applicants(age, has_license):
    
    if age > 21 and has_license.lower()=='y':
        print('Hired :) ')
    else:
        print('Rejected :( ')


if __name__ == "__main__":
    age = int(input('input your age: '))
    has_license = input('do you have a license? y/n: ')
    check_applicants(age, has_license)
    