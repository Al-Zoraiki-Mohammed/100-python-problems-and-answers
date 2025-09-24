"""Task33"""

def calc_discount(purchase_price, discount=0):
    if purchase_price > 50 and purchase_price <= 100:
        discount = 0.05   
    elif purchase_price > 100 and purchase_price <= 200:
        discount = 0.1
    elif purchase_price > 200:
        discount = 0.15
    purchase_price *= (1 - discount)
    return discount, purchase_price

if __name__ == '__main__':
    purchase_price = int(input("Enter the purchase price: "))
    discount, amount = calc_discount(purchase_price)
    print(f"Your discount is {discount * 100 }%, the amount to be paid is {amount}$")
