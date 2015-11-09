# Lecture 20

"Consumption of Time"

def factors(n):
	Slow: test each k from 1 through n
	Fast: Test each k from 1 to square root n 
		  For each k, n/k is also a factor
		  Time: greatest integer less than sqrt(n)

def factors_fast(n):
	sqrt_n = sqrt(n)
	k, total = 1, 0
	while k < sqrt_n:
		if divides(k,n):
			total += 2
		k += 1
	if k**2 == n:
		total += 1
	return total

"Consumption of Space"

Which environment frames do we need to keep during evaluation?
Memory that is used for other values and frames can be recycled

"Orders of Growth"

A method for bounding the resources used by a function by the "size" of a problem

n: size of the problem
R(n): measurement of some resource used (time or space)

k_1*f(n) ≤ R(n) ≤ k_2*f(n)
