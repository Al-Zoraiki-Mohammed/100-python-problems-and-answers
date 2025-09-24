"""Task35"""
def get_revenue(first_week, second_week, price):
    if first_week < second_week:
        print(
            "In the second week, the cinema sold {} more tickets than in the first one.".format(
                second_week - first_week,
            ),
        )
    elif first_week > second_week:
        print(
            "In the first week, the cinema sold {} more tickets than in the second one.".format(
                first_week - second_week,
            ),
        )
    else:
        print(
            "The cinema sold the same number of tickets in the first week as in the second week."
        )
    print("The total cinema's revenue for two weeks was ${}.".format(
        (second_week + first_week) * price
    ))


if __name__ == '__main__':
    first_week = int(input("Input the number of tickets sold in the first week: "))
    second_week = int(input("Input the number of tickets sold in the second week: "))
    price = int(input("Enter the ticket price: "))
    print("{} tickets were sold during the first week".format(first_week))
    print("{} tickets were sold during the second week".format(second_week))
    get_revenue(first_week, second_week, price)
    