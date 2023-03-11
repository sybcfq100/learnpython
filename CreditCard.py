"""A consumer credit card."""

def __init__(self, custom, bank, acnt, limit):
    """create a new credit card instance
    The initial balance is zero
    customer the name of the customer 
    bank
    acnt
    limit
"""
    self._customer = custom
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

def get_customer(self):
    """return name of customer"""
    return self._customer

def get_bank(self):
    """return name of bank"""
    return self._bank

def get_account(self):
    """return the card identifying number """
    return self._account


def get_limit(self):
    """return current credit limit"""
    return self._limit

def get_balance(self):
    """return current balance"""
    return self._balance

def charge(self, price):
    """ Charge given price to the card, assuming sufficient credit limit.
    Return True if charge was processed; False if charge was denied"""
    if price + self._balance > self._limit:
        return False
    else:
        self._balance += price
        return True

def make_payment(self, amount):
    self._balance -=amount