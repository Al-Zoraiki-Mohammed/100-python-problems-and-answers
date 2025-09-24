"""Task:12"""

def read_data(no_st):
    student_marks = {}
    for i in range(no_st):
        name, *str_scores = input(f'Enter Student name {i+1} followed by scores: ').split()
        scores = [float(item) for item in str_scores]
        student_marks[name] = scores
    return student_marks

def get_average(student_marks):
    query_name = input('Type name to get his/her average: ')
    sum = 0
    for mark in student_marks[query_name]:
        sum +=mark
    average = sum/len(student_marks[query_name])
    return f'{average:.2f}'


if __name__ == '__main__':
    no_st = int(input('Enter number of students: '))
    student_marks = read_data(no_st)

    average = get_average(student_marks)
    print(average)
