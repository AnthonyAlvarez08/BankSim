'''
just a testing ground for now
'''


from BankAccount import *

wah = PersonalAccount('Fake Fakeson', 0.06)

wah.deposit(500.878, Types.checking)
wah.withdrawal(600.6586785, Types.checking)

wah.statement()

hehe = StudentAccount('Fake Fakesonson', wah, 'University of Anime Girls', 0.06)
hehe.deposit(4523423.45, Types.savings)
hehe.deposit(53452343254234.45, Types.checking)
hehe.statement()