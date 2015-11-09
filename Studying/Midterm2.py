def make_prime_generator():
	 n= 2 
	 def primes():
	 	nonlocal n
	 	found_prime = False
	 	while not found_prime:
	 		n += 1
	 		found_prime = True
	 		for i in range(2,n):
	 			if n % i == 0:
	 				found_prime = False
	 	return n
	 return primes

