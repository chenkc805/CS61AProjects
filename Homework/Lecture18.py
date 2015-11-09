# Lecture18

""" An object value should behave like the kind of data it is meant to represent

For instance, by producing a string representation of itself

In Python, all objects produce two string representations:

repr - returns a python expression (a string) that evaluates to an equal object

for most object types, eval(repr(object)) == object

str - result of calling str on the value of an expression is what python prints using the print function

import datetime
today = datetime.date(2014,10,13)
repr(today)
str(today) """

# Polymorphic Functions - A function that applies to many different forms of data
"""
repr invokes a zero-argument method __repr__ on its argument

>>> today.__repr__()
'datetime.date(2014,10,13)'
"""

# Implementing repr and str
"""
The behavior of repr is slightly more complicated than invoking __repr__ on its argument:
- An instance attribute called __repr__ is ignored! only class attributes are found
"""

# Property Method
"""
Often, we want the value of instance attributes to stay in sync

The @property decorator on a method designates that it will be called whenever it is looked up on an instance
"""

class Rational:
	def __init__(self,numer,denom):
		self.numer = numer
		self.denom = denom

	def __repr__(self):
		return 'Rational({0},{1})'.format(
					self.numer, self.denom)

	@property
	def float_value(self): #recompute the fload value each time its looked up
		return self.numer / self.denom


""" An Interface for Complex Numbers
All complex numbers should have real and imag components
All components 
