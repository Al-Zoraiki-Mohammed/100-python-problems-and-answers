"""#Task49:"""
def log_in(real_pin_code, balance, max_attempts=5):
    entered_pin_code = input('Type your pin code: ')
    while real_pin_code != entered_pin_code and  max_attempts >=1:
        max_attempts -= 1
        entered_pin_code = input(f'''incorrect pin code:)
                        you have {max_attempts } attempts: ''')
    if max_attempts == 0:
        print('Sorry, your card is locked')
    else:
        print(f'Your balance is {balance}')


if __name__ == "__main__":
    real_pin_code = '1234'
    max_attempts = 5
    balance = '5000$'
    log_in(real_pin_code,balance, max_attempts)
    