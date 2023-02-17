def make_withdraw(balance):
    '''return a withdraw function with a starting balance'''
    def withdraw(amount):
        nonlocal balance # declare the name 'balance' nonlocal at the top of the body of the function in whitch it is re-assigned
        if amount > balance:
            return 'Insuficient funds'
        balance = balance - amount # re-bind balance in the first non-local frame in which is was bound previously
        return balance
    return withdraw

#  withdraw = (make_withdraw(100))
print(make_withdraw(100)(10))
