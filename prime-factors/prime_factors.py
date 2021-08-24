import math

def factors(value):
	factors = []
	while value > 1:
		for prime in get_primes():
			if value % prime == 0:
				value /= prime
				factors.append(prime)
				break
	return factors
	
def get_primes():
	n = 2
	primes = []
	while True:
		for prime in primes:
			if n % prime == 0:
				break
		else:
			primes.append(n)
			yield n
		n += 1
