# CS 61A Fall 2014
# Name: Kevin Chen  
# Login: cs61a-sj

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.remaining_money = 0
        self.present_stock = 0

    def vend(self):
        if self.present_stock == 0:
            return 'Machine is out of stock.'
        if self.remaining_money < self.cost:
            return 'You must deposit $' + str(self.cost - self.remaining_money) + ' more.'
        if self.remaining_money > self.cost:
            self.change = self.remaining_money - self.cost
            self.remaining_money = 0
            self.present_stock -= 1
            return 'Here is your ' + self.name + ' and $' + str(self.change) + ' change.'
        else:
            self.remaining_money = 0
            self.present_stock -= 1
            return 'Here is your candy.'

    def deposit(self,amount):
        if self.present_stock == 0:
            return 'Machine is out of stock. Here is your $' + str(amount) + '.'
        else:
            self.remaining_money += amount
            return 'Current balance: $' + str(self.remaining_money)

    def restock(self,stock):
        self.present_stock += stock
        return 'Current ' + self.name + ' stock: ' + str(self.present_stock)

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, an_object):
        self.an_object = an_object

    def ask(self, request, *args):
        if 'please' not in request:
            return 'You must learn to say please first.'
        else:
            new_request = request[7:]
            if hasattr(self.an_object, new_request):
                return getattr(self.an_object, new_request)(*args)
            return 'Thanks for asking, but I know not how to ' + new_request






















