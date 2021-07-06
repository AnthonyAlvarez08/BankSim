from BankAccount import PersonalAccount, Types

wah = PersonalAccount('Fake Fakeson', 0.06)

wah.deposit(500.878, Types.checking)
wah.withdrawal(600.6586785, Types.checking)

wah.statement()