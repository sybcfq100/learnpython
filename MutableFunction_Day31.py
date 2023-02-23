#  def make_withdraw(balance):
    #  '''return a withdraw function with a starting balance'''
    #  def withdraw(amount):
    #      nonlocal balance # declare the name 'balance' nonlocal at the top of the body of the function in which it is re-assigned
    #      if amount > balance:
    #          return 'Insufficient funds'
    #      balance = balance - amount # re-bind balance in the first non-local frame in which is was bound previously
    #      return balance
    #  return withdraw
    #
#  withdraw = (make_withdraw(100))
#  print(withdraw(10))
#  print(withdraw(35))
#  print(withdraw(26))
#  """
#  what is the meaning or function of nonlocal
#  """

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x += 1
            return x + y + z

        return h

    return g

a = f(1)
b = a(2)
total = b(3) + b(4)
#  print(b(3))
#  print(b(4))
print(total)
