""" Lecture 17

<instance>.<method_name>

"""

# Inheritance
""" 

class <Name>(<Base Class>):
	<suite>

The subclass inherits attributes of its base class
subclass can override attributes of the base class
"""

>>> ch = CheckingAccount('Tom')
>>> ch.interest		# Lower interest rate for checking accounts
0.01
>>> ch.deposit(20)	# Deposites are the same
20
>>> ch.withdraw(5)	# Withdrawals incur a $1 fee
14

" Most behavior is shared with the base class Account, except the $1 fee "

class CheckingAccount(Account):
	""" A bank account that charges for withdrawals."""
	withdraw_fee = 1
	interest = 0.01
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_fee)

>>> ch = CheckingAccount('Tom') # Calls Account.__init__
>>> ch.interest 				# Found in Checking Account
0.01
>>> ch.deposit(20)				# 
20
>>> ch.withdraw(5)
14

# Designing for Inheritance
""" 

- Don't repeat yourseif; use existing implementations
- Attributes that have been overridden are still accessible via class objects
- Look up attributes on instances whenever possible

"""

#Inheritance and Compositions
"""

Object-oriented programming shines when we adopt the metaphor
Inheritance is best for representing is-a relationships

ex)
class Bank:
	def __init__(self):
		self.accounts = []

	def open_account(self, holder, amount, account_type = Amount):
		account = account_type(holder)
		account.deposit(amount)
		self.accounts.append(account)
		return account

"""

# Multiple Inheritance
"""




























