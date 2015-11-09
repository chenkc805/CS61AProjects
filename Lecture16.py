# Object Oriented Programming
""" A method for organizing programs
* Data Abstraction
* Bundling together information and related behavior

A metaphor for computation using distributed state
* Each object has its own local state
* Each object also knows how to manage its own local state, based on method calls
* Method calls are messages passed between objects
* Several objects may all be instances of a common type
* Different types may relate to each other
"""

""" Classes
* A class serves as a template for all its instances
"""

# The Class Statement

class <name> :
	<suite>

class Clown:
	nose = 'big and red'
	def dance():
		return 'No thanks'

Clown.nose 
'big and red'

# Object Construction
a = Account('Jim') # a is an instance

""" When a class is called:
1. A new instance of that class is created: 
2. The __init__ method of the class is called with the new object as its first argument (named self),
	along with any additional arguments provided in the call expression.
	
