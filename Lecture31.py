# Streams

# Motivation
"""
Recall that sometimes we need to represent a sequence of values 
whose length is bigger than the amount of space we have on our 
computer.

In Python, we usually solve this by using iterators and generators
However, there is another way
"""

# Stream
"""
A stream is a data structure created through a first and a compute_rest
The first can be any data value. The compute_rest must be a Thunk* that 
returns anotherstream. Each Stream has a first and a rest, just like 
Linked Lists.

Streams can represent infinite linked Lists
"""

a = Stream(1, lambda: Stream(2, lambda: Stream.empty))

first_k(a,2)

ones = Stream(1, lambda: ones)

def integer_stream(first = 1):
	def compute_rest():
		return integer_stream(first+1)
	return Stream(first, compute_rest)

def add_streams(s1, s2):
	def compute_rest():
		return add_streams(s1.rest, s2.rest)
	return Stream(s1.first+s2.first, compute_rest)

fib_stream = Stream(0 , lambda: Stream(1,lambda: add_streams(fib_stream, fib_stream.rest)))

# Higher Order Functions on Streams
"""
Write filter_stream, which takes in a predicate and a stream 
and outputs a new stream that only has the elements that predicate.
"""


is_odd = lambda x: x%2 == 1
odds = filter_stream(is_odd, nats)
first_k(odds, 4)

def filter_stream(f, s):
	def compute_rest():
		return filter_stream(fn, s.rest)
	if fn(s.first):
		return Stream( s.first ,compute_rest)
	else:
		return compute_rest()

class Stream:
	class empty:
		def __repr__(self):
			return 'Stream.empty'
	empty = empty()

	def __init__(self, first, compute_rest = lambda: Stream.empty):
		assert callable(compute_rest), 'compute_rest must be callable.'
		self.frst = first
		self._compute_rest = compute_rest

	@property
	def rest(self):
		if self._compute_rest is not None:
			self._rest = self._compute_rest()
			self._compute_rest = None
		return self._rest

def sieve(s):
	return Stream(s.first, lambda: sieve(stream_filter(lambda x: x%s.first != 0, s.rest )))
nats = integer_stream(2)
primes = sieve(nats)
first_k(primes,10)


























