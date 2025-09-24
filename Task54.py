
"""Task54"""
def reverse_from_string(number):
    return number[::-1]


def revese_number_inplace(number):
    number_list = list(number)
    number_list.reverse()
    return "".join(number_list)


def reverse_number_slicing(number):
    number_list = list(number)
    revesed_list = number_list[::-1]
    return "".join(revesed_list)


def reversed_number(number):
    number_list = list(number)
    return "".join(reversed(number_list))


def reverse_from_scratch(number):
    reverse_number = ""
    for i in range(len(number)-1,-1,-1):
       reverse_number += number[i]
    return reverse_number


def reverse_as_integer(number):
    number_int = int(number)
    reverse_str = ""
    for i in range(len(number)):
        reverse_str += str(number_int % 10)
        number_int = int(number_int /10)
    return reverse_str                        


def print_reversed_number(number):
    print(reverse_from_string(number))
    print(revese_number_inplace(number))
    print(reverse_number_slicing(number))
    print(reversed_number(number))
    print(reverse_from_scratch(number))
    print(reverse_as_integer(number))
   

if __name__ == "__main__":
    number = input("Type a number: ")
    print_reversed_number(number)
