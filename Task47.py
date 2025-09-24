"""#Task47:"""
def calc_total_bill(bill_value, service_fee=0.1, tax=0.15):
    bill_value += (bill_value * service_fee)
    total_bill = bill_value * tax + bill_value
    print(f'Total bill value is {total_bill}')


if __name__ == "__main__":
    bill_value = float(input('Enter  bill value: '))
    calc_total_bill(bill_value, service_fee=0.1, tax =0.15)
    