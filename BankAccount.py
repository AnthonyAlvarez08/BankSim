'''
enum for account types
'''
class Types:
    checking = 'checking'
    savings = 'savings'
    reserve = 'reserve'

'''
super class for a regular account
'''
class BankAccount:

    def __init__(self, owner : str, interest : float):
        self._owner = owner
        self._interest = interest
        self._accounts = dict()

        # all accounts will have at least a checking account
        self._accounts[Types.checking] = 0.0

    def deposit(self, amount : float, account : Types):
        

        # handle not using a proper account
        if not account in self._accounts.keys():
            raise ValueError(Types)

        self._accounts[account] += amount


    def withdrawal(self, amount : float, account : Types):

        # handle not using a proper account
        if not account in self._accounts.keys():
            raise ValueError(Types)

        # raise a warning about withdrawing too much
        if amount > self._accounts[account]:
            print(f'{account} account will go to negative value after this transaction\n')

        self._accounts[account] -= amount

    # prints an account statement
    def statement(self):
        print(f'Bank statement for {self._owner}')
        for i in self._accounts.keys():
            print(f'{i}: ${round(self._accounts[i], 2)}')
        print()

    
    def __repr__(self):
        return self.statement()


class PersonalAccount(BankAccount):

    def __init__(self, owner : str, interest : float):
        super().__init__(owner, interest)
        self._accounts[Types.savings] = 0.0
        self._accounts[Types.reserve] = 0.0


class BusinessAccount(BankAccount):

    def __init__(self, owner : str, business : str, interest : float):
        super().__init__(owner, interest)
        self._business = business

    # override superclass statement
    def statement(self):
        print(f'Bank statement for {self._business}')
        for i in self._accounts.keys():
            print(f'{i}: ${round(self._accounts[i], 2)}')
        print()


class StudentAccount(PersonalAccount):
    pass