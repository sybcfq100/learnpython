"""A consumer credit card."""


class CreditCard:

    def __init__(self, custom, bank, account, limit):
        """create a new credit card instance
        The initial balance is zero
        customer the name of the customer
        bank
        account
        limit
        """
        self._customer = custom
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """return name of customer"""
        return self._customer

    def get_bank(self):
        """return name of bank"""
        return self._bank

    def get_account(self):
        """return the card identifying number"""
        return self._account

    def get_limit(self):
        """return current credit limit"""
        return self._limit

    def get_balance(self):
        """return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied"""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """process customer payment that reduces balance."""
        self._balance -= amount


# if __name__ == '__main__':
#     wallet = []
#     wallet.append(CreditCard(
#         "John Bowman", "California Savings", 1234567, 5000))
#     wallet.append(CreditCard(
#         "John Bowman", "California Federal", 3485039, 3000))
#     wallet.append(CreditCard(
#         "John Bowman", "California Finance", 5391037, 2500))
#     for val in range(1, 17):
#         wallet[0].charge(val)
#         wallet[1].charge(2*val)
#         wallet[2].charge(3*val)

#     for c in range(3):
#         print('Customer = ', wallet[c].get_account())
#         print('Bank = ', wallet[c].get_bank())
#         print('Account = ', wallet[c].get_account())
#         print('Limit = ', wallet[c].get_limit())
#         print('Balance = ', wallet[c].get_balance())
#         while wallet[c].get_balance() > 100:
#             wallet[c].make_payment(100)
#             print('New balance = ', wallet[c].get_balance())
#         print()


class PredatoryCreditCard(CreditCard):
    # An extension to CreditCard that compounds interest and fees.

    def __init__(self, customer, bank, account, limit, apr):  # 成员函数
        """create a new predatory credit card instance
        customer the name of the customer
        bank
        account
        limit
        apr
        """
        super().__init__(
            customer, bank, account, limit
        )  # 调用继承构造函数执行大部分初始化处理，这样就不用重复写customer等4个参数
        self._apr = apr  # 扩展---构造参数年利率

    def charge(
        self, price
    ):  # 定义的新方法，成员函数--取决于对继承方法的调用，调用函数返回值表明是否收费成功,我们检查返回值，决定是否评估费用
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False and assess $5 fee if charge was denied
        """
        success = super().charge(
            price
        )  # 调用继承方法，如果超出限额，返回False，否则返回True
        if not success:
            self._balance += 5  # 收取5元手续费
        return success  # 调用者期望返回值

    def process_month(self, apr):  # 成员函数 - 新方法，只有self，没有依赖继承的版本
        """Assess monthly interest and compute payment
        Return True if payment is due; False if payment is not due"""
        if self._balance > 0:  # balance 表示有欠款，需要收利息
            monthly_factor = pow(1 + self._apr, 1 / 12)  # 月收取利息因子
            self._balance *= monthly_factor  # 收取金额


acc = PredatoryCreditCard("Uday", "SBI", "123456789", 1000, 15)
print(acc.charge(500))
print(acc.get_balance())
print(acc.process_month(15))
