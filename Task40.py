"""Task40"""
def check_applicants(has_refrence, age=0, has_license ='y'):
    if has_refrence.lower() == 'y':
        print('Hired :) ')
    else:
        age = int(input('How old are you ?: '))
        has_license = input('Do you have a license? y/n: ')

        if age > 21 and has_license.lower()=='y':
            print('Hired :) ')
        else:
            print('Rejected :( ')


if __name__ == "__main__":
    has_refrence = input('Do you have a refrence? y/n: ')
    check_applicants(has_refrence)
