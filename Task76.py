""""""
accounts = {'1': {'Name': 'Mohammed', 'PIN_code': '123', 'balance': '40000$' }, 
            '2': {'Name': 'Ali', 'PIN_code': '456', 'balance': '30000$' }}


def print_client_details(client):
    if client != None:
        for key, value in client.items():
            print(f'{key}: {value}')
    else:
        print('No client found')


def find_client(account_no):
    if account_no in accounts.keys():
        client = accounts.get(account_no)
        print_client_details(client)


def delete_account(account_no):
    if account_no in accounts:
        accounts.pop(account_no, 'client not found')
        print(f'client  with account number: {account_no} is deleted')
    else:
        print(f'account with account number {account_no} is not found')


def add_client(account_no, **kwargs):
    while account_no in accounts.keys():
        print(f'account number { account_no} is already asociated with a client:( ')
        account_no = input('Type another account number add: ').strip()
    
    if account_no != None and kwargs != None:
        accounts[account_no] = kwargs
        print(f'account with account number: {account_no} is added')
    else: 
        print(f'account number: {account_no} or account name is not valid ')


if __name__ == '__main__':
    print(f'Initial accounts are: {accounts}')

    account_no = input('Type account number to search for: ').strip()
    find_client(account_no)

    account_no = input('Type account number to delete: ').strip()
    delete_account(account_no)
    print(f'Updated accounts are: {accounts}')
   
    account_no = input('Type account number add: ').strip()
    account_name = input('Type account name to add: ').strip()
    PIN_code = input('Type account PIN code to add: ').strip()
    balance = input('Type account balance to add: ').strip()
    add_client(account_no=account_no,
                account_name=account_name,PIN_code=PIN_code, balanc=balance)
    print(f'Updated accounts are: {accounts}')
    