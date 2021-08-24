import secrets
from itertools import cycle
import string

class Cipher:

	def __init__(self, key=None):
		if not key:
			key = key or "".join(secrets.choice(string.ascii_letters).lower() for _ in range(100))
		self.key = key

	def encode(self, text):
		# addition yields >= 2*97, so subtract those to get to [0, 2*26], mod 26 to wrap around, and then transpose up to >= 97
	    return "".join(chr((ord(c)+ord(k) - 2*97) % 26 + 97) for k, c in zip(cycle(self.key), text))

	def decode(self, text):
		# Subtraction yields >= -26, so add 26 to get to [0, 2*26], mod 26 to wrap around, and then transpose up to >= 97
	    return "".join(chr((ord(c)-ord(k) + 26) % 26 + 97) for k, c in zip(cycle(self.key), text))
