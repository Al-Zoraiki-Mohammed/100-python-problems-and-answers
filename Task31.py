"""Task31"""

def check_speed_violation(miles, time=0.5, speed_limit=45):   
    if miles / time > speed_limit:
        print("The driver violated the traffic rules")
    else:
        print("The driver didn't violate the traffic rules")


if __name__ == '__main__':     
    miles = 0
    while miles <= 0: 
        miles = float(input("Enter the number of miles: "))
    check_speed_violation(miles )
    