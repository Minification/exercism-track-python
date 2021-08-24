import re

def is_valid(isbn) -> bool:
	isbn_no_hypthens = re.sub(r"\-", "", isbn)
	isbn_structure_regex = re.compile(r"\d{9}(\d|X)$")
	if isbn_structure_regex.match(isbn_no_hypthens) == None:
		return False
	return checksum(isbn_no_hypthens) % 11 == 0
    
def checksum(numbers_string: str) -> int:
	numbers_list = [
		10 if character == "X" else int(character)
		for character in numbers_string
	]
	return sum(t[0] * t[1] for t in zip(numbers_list, range(10, 0, -1)))
