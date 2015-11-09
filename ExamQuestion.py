from operator import add , mul 
def square(x):
	return mul(x, x)
def delay(arg): 
	print('delayed') 
	def g():
		return arg 
	return g