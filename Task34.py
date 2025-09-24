"""Task34"""

def get_data(num_of_student=15):
    scores = []
    for i in range (num_of_student):
        scores.append(int(input(f'Enter score for student no_{i+1}: ')))
    return scores


def get_grades(scores):
    grades = {'F':0, 'P':0, 'S':0, 'G':0, 'E':0}
    for score in scores:
        if score <= 50: grades['F'] = grades['F'] + 1
        elif score <= 65: grades['P'] = grades['P'] + 1
        elif score <= 79: grades['S'] = grades['S'] + 1
        elif score <= 89: grades['G'] = grades['G'] + 1
        elif score <= 100: grades['E'] = grades['E'] + 1
    return grades


def print_number_of_grades(grades):
    for grade, num_of_grade in grades.items():
        print(f'grade: {grade} = {num_of_grade} students')


if __name__ == "__main__":
    scores = get_data()
    grades = get_grades(scores)
    print_number_of_grades(grades)
