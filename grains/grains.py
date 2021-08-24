def square(number):
	if number > 64 or number <= 0:
		raise ValueError("Number must be in range(1, 65)!")
	return 2 ** (number-1)


def total():
	return 2 ** 64 - 1
