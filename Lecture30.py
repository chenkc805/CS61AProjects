# Lecture 30

# Implicit Sequences
"""
An implicit sequence is a representation of sequential data that does not explicitly store each element

Example: The built-in range class represents consecutive integers. We remember the start and end, but nothing in between.
range(-2,2) --> -2, -1, 0, 1

We can build a class that works like range.
"""

class Range:
	""" Implicit sequence of consecutive integers.

	>>> r = Range(3,12)
	>>> len(r)
	9
	>>> r[3]
	6
	"""
	def __init__(self,start,end = None):
		if end is None:
			start, end = 0, start
		self.start = start
		self.end = end

	def __len__(self):
		return max(0, self.end -self.start)

	def __getitem__(self, k):
		if k >= len(self):
			raise IndexError('index out of range')
		return self.start + k

# Iterator Interface
""" 
An iterator is an object that can provide the next element of a sequence
The __next__ method of an iterator returns the next element
The build-in next function invokes the __next__ method on its argument
If there is no next element, then the __next__ method of an iterator should raise a StopIteration exception
"""

class RangeIter:
	def __init__(self, start, end):
		self.next_number = start
		self.end = end

	def __next__(self):
		if self.next_number >= self.end:
			raise StopIteration
		result = self.next _number
		self.next_number += 1
		return result

# Iterables and Iterators
"""
Iterators: Mutable objects that track a position in a sequence, advancing on __next__
Iterable: Represents a sequence and returns a new iterator on __iter__

LetterIter is an iterator: 	LetterIter('a', 'e')
Letters is iterable: 		Letters ('a', 'e')
"""

class LetterIter:
	def __init__(self, start='a', end='z'):
		self.next_number = start
		self.end = end

	def __next__(self):
		if self.next_number >= self.end:
			raise StopIteration
		result = self.next _number
		self.next_number = chr(ord(result)+1)
		return result

class Letters:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __iter__(self):
		return LetterIter(self.start, self.end)

# Capitalized 
caps = map(lambda x: x.upper(), s)

# For Statement
"""
for <name> in <expression>:
	<suite>

1. Evaluate the header <expression>, which must evaluate to an ***iterable*** object
2. 
"""

# Generators and Generator Functions
"""
A generator is an iterator, created by a generator function
A generator function is a function that yields values instead of returning them
A normal function returns once; a generator function yields multiple times
When a generator function is called, it returns a generator that iterates over yields

Yield pauses the while statement
"""

def letters_generator(next_letter, end):
	while next_letter < end:
		yield next_letter
		next_letter = chr(ord(next_letter)+1)
















