import re

class Luhn:
	def __init__(self, card_num: str) -> None:
		# Collect only the digits.
		digits = [int(d) for d in card_num if d.isdigit()]
		# Kind of an offset. For even length numbers,
		# we have to start at index 0, then 2, then 4...,
		# whereas for odd length numbers, we have to start
		# at index 1, 3, 5...
		mod_result = len(digits) % 2
		# Double and wrap every second number in a forward pass.
		mapped = [2*d - 9*(d > 4) if i % 2 == mod_result else d for i, d in enumerate(digits)]
		self.__valid = len(digits) > 1\
						and not bool(re.search(r'[^\d\s]+', card_num))\
						and sum(mapped) % 10 == 0
        

	def valid(self) -> bool:
		return self.__valid
