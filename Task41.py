""" Task41 """
def read_marks(number_of_marks):
    """read marks and return the sum and number_fails"""
    sum = 0
    number_of_fails = 0
    for i in range(number_of_marks):
        mark = int(input(f'enter mark {i}: '))
        if mark < 50:
            number_of_fails = number_of_fails + 1
        sum += mark
    return sum, number_of_fails


def calculate_average(number_of_marks):
    """Calculate average"""
    sum, number_of_fails = read_marks(number_of_marks)
    average = sum/number_of_marks
    if number_of_fails > 0:
        print(f"your average is {average}, however you failed in {number_of_fails} subjects")
    else:
        print(f" Congrats, you get pass, and your average is {average}")


if __name__ == "__main__":
    number_of_marks = int(input('enter number of marks: '))
    calculate_average(number_of_marks)
    