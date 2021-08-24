def primes(limit):
	potential_primes = [True] * (limit+1)
	# 0 and 1 are not primes
	potential_primes[0:2] = [False] * 2
	primes = []
	for counter, value in enumerate(potential_primes):
		if value:
			# If we reached this, the current value is prime
			primes.append(counter)
			# Mark all multiples of the current prime as composite
			potential_primes[counter*2:limit+1:counter] = [False] * len(range(counter*2, limit+1, counter))
	return primes
