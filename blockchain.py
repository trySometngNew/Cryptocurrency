# Initializing our blockchain

open_transactions = []
owner = 'Max'
genesis_block = {
            'previous_hash':'', 
            'index' : 0, 
            'transactions' : []
            }
blockchain = [genesis_block]


def get_last_blockchain_value():
    ''' Returns last value of our blockchain. '''
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    ''' Append a new value as well as last blockchain value to the blockchain. 
    
    Arguments:
        : sender : Sender of the transaction.
        : recipient : Recipient of the transaction.
        : amount : The amount that should be added. (default = 1.0)
    '''
    transaction = {'sender': sender, 
                   'recipient': recipient, 
                   'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]

    hashed_block = '-'.join(str(last_block[key]) for key in last_block)

    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block = hashed_block + str(value)
    print(hashed_block)

    block = {
            'previous_hash':hashed_block, 
            'index' : len(blockchain), 
            'transactions' : open_transactions
            }
            
    blockchain.append(block)

def get_transaction_value():
    ''' Returns the input of the user (a new transaction amount) as a float. '''
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else: 
        print('-' * 20)

def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        if blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break        
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     if block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    print('Blockchain Validity: ', is_valid)
    return is_valid

waiting_for_input = True

while waiting_for_input:
    print('Please Choose: ')
    print('1. Add a new transaction value.')
    print('2. Mine a new block.')
    print('3. Output the blockchain blocks.')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    # if not verify_chain():
    #     print('Invalid Blockchain!')
    #     break
else:
    print('User left!')

print('Done!')