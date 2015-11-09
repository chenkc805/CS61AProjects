# Measuring Efficiency

def count(f):
	def counted(n):
		if n == 1:
			counted.call_count += 1
		return f(n)
	counted.call_count = 0
	return counted

@count
def fib(n): 
	if n == 0: 
		return 0
	elif n == 1: 
		return 1
	else: 
		return fib(n-2) + fib(n-1)

def memo(f):
	cache = {}
	def memoized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized
