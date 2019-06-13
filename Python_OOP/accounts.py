"""
A Bank account example from inspired by the example in "anandology.com"
"""

from pprint import pprint as pp

class BankAccount:


    # today = "02/20/2017"

    def __init__(self):
        self.balance = 0
        self.transactionList = []
        print("Thank you for opening an account with us!")

    def withdraw(self, amount=0):

        self.balance -= amount
        print(self)

    def deposit(self, amount):

        something = "Hello There"

        self.balance += amount
        print(self)

    def __str__(self):
        about = "=> Balance = {}".format(self.balance)
        return about

    def addValues(self, *args):

        for value in args:

            if value >= 0:
                print("Depositing {0}".format(value))
                self.deposit(value)
            else:
                print("Withdrawing {0}".format(value))
                self.withdraw(value)

    def addTransactions(self, **kwargs):

        for transaction, value in kwargs.items():

            if transaction.capitalize() == "Deposit":
                print("Depositing {0}".format(value))
                self.deposit(value)
            else:
                print("Withdrawing {0}".format(value))
                self.withdraw(value)


class MinimumBalanceAccount(BankAccount):
    """
    A bank account that must have a minimum. Error checking involved at withdrawal.
    """

    def __init__(self, minimum_balance):

        # super().__init__()
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance
        self.balance = minimum_balance

    def deposit(self, amount):
        pass

    def _withdraw(self, amount):

        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

    def printSpecialFunctions(self):

        print("MinimumBalanceAccount.__doc__: {}".format(MinimumBalanceAccount.__doc__))
        print("MinimumBalanceAccount.__name__: {}".format(MinimumBalanceAccount.__name__))
        print("MinimumBalanceAccount.__module__: {}".format(MinimumBalanceAccount.__module__))
        pp(self.__dict__)

class BusinessAccount(BankAccount):
    """
    A bank account with additional attributes.
    """

    # User: MaxAmount
    accountUsers = {}

    def __init__(self, startingBalance, businessName):

        BankAccount.__init__(self)

        self.balance = startingBalance
        self.businessName = businessName

    def addSingleUser(self, maxValueToWithdraw, userName):

        if userName not in self.accountUsers:
            self.accountUsers[userName] = maxValueToWithdraw
        else:
            print("User '{}' already exists.".format(userName))

    def addMultipleUsers(self, maxValueToWithdraw, *args):

        # You might want to do some error checking.
        for userName in args:
            self.addSingleUser(maxValueToWithdraw, userName)

    def modifyData(self, **kwargs):

        pp(kwargs.keys())
        pp(kwargs.values())


if __name__ == "__main__":

    myAccount = BankAccount()
    print(myAccount)

    myAccount.deposit(1000)
    myAccount.withdraw(1100)

    studentAccount = MinimumBalanceAccount(100)
    studentAccount.deposit(1000)
    studentAccount.withdraw(1000)
    studentAccount.withdraw(700)

    # Other important functions.
    hasattr(studentAccount, 'balance')      # Returns true if attribute exists
    getattr(studentAccount, 'balance')      # Returns value of attribute
    setattr(studentAccount, 'balance', 800) # Set attribute to value.

    # CAREFUL WITH THAT!!!!!
    # delattr(studentAccount, 'balance')      # Delete attribute
    # getattr(studentAccount, 'balance')
    # studentAccount.deposit(1000)

    myBusiness = BusinessAccount(10000, "TheCafe")

    myBusiness.addSingleUser(1000, "Alex Gheith")

    # Using *args
    myBusiness.addMultipleUsers(1200, "Mark Johnson", "Bill Gates", "Lisa Mike", "Sally T.")
