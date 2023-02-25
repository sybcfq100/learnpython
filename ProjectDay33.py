#  class Account:
#      interest = 0.02
#      def __init__(self, account_holder):
#          self.balance = 0
#          self.holder = account_holder
#
#      def deposit(self, amount):
#          self.balance += amount
#          return self.balance
#
#      def withdraw(self, amount):
#          if amount > self.balance:
#              return 'Insufficient funds'
#          self.balance -= amount
#          return self.balance
#
#  class CheckingAccount(Account):
#      interest = 0.01
#      withdraw_fee = 1
#      def withdraw(self, amount):
#          return Account.withdraw(self, amount + self.withdraw_fee)
#
#  #  tom_account = CheckingAccount('Tom')
#  #  ntd = tom_account.deposit
#  #  td = tom_account.deposit(100)
#  #  td = tom_account.withdraw(25)
#  #  print(td)
#  #  tom_account.interest = 0.08
#  #  Account.interest = 0.05
#  #  print(tom_account.interest)
#
#  class Bank:
#      def __init__(self):
#          self.accounts = []
#
#      def open_account(self, holder, amount, kind=Account):
#          account = kind(holder)
#          account.deposit(amount)
#          self.accounts.append(account)
#          return account
#
#      def pay_interest(self):
#          for a in self.accounts:
#              a.deposit(a.balance * a.interest)
#
#      def too_big_to_fail(self):
        #  return len(self.accounts) > 1


class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)

class C(B):
    def f(self, x):
        return x
    
