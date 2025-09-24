"""Task75"""

accounts = {'1':'Mohammed', '2': 'Ahmed', '3': 'Omar'}


def find_cleint(account_no):
    for key, value in accounts.items():
        if key == account_no:
            client = value
            return client
    return 'client not found'


def find_client_v2(account_no):
    return accounts.get(account_no)
   

def delete_account(account_no):
    accounts.pop(account_no, 'client not found')
    print(f'client  with account number: {account_no} is deleted')


def add_client(account_no, name):
    while account_no in accounts.keys():
        print(f'account number { account_no} is already asociated with a client:( ')
        account_no = input('Type another account number add: ').strip()
    
    if account_no != None and name != None:
        accounts[account_no] = name
        print(f'account with account number: {account_no} and name: {account_name} is added')
    else: 
        print(f'account number: {account_no} or account name: {account_name} is not valid ')


if __name__ == "__main__":

    print(f'Initial accounts are: {accounts}')

    account_no = input('Type account number to search for: ').strip()
    client = find_cleint(account_no)
    client_v2 = find_client_v2(account_no)
    print(client_v2)

    account_no = input('Type account number to delete: ').strip()
    delete_account(account_no)
    print(f'Updated accounts are: {accounts}')

    account_no = input('Type account number add: ').strip()
    account_name = input('Type account name to add: ')
    add_client(account_no, account_name)
    print(f'Updated accounts are: {accounts}')
