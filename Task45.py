"""Task45"""
def find_grade(mark):
    if mark >=0 and mark < 50:
        print('Fail')
    elif mark >=50 and mark < 65:
        print('Pass')
    elif mark >=65 and mark < 80:
        print('Good')
    elif mark >= 80 and mark < 90:
        print('Very Good')
    elif mark >=90 and mark <= 100:
        print('Excellent')


if __name__ == "__main__":
    mark = int(input('Type your grade: '))
    while mark < 0 or mark > 100:
        mark = int(input('Type valid grade between 0 and 100: '))
    find_grade(mark)
    