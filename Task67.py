"""Task67"""
def my_round(number):
    fraction = number - int(number)
    if fraction >= 0.5:
        return int(number + 1)
    else:
        return int(number)


if __name__ == "__main__":
    number = float(input('Type a number to round: '))
    print(my_round(number))
