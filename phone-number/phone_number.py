import re

class PhoneNumber:
	def __init__(self, number: str) -> None:
		# Only digits are important, so find them
		numbers_array = re.findall(r'\d+', number)
		extracted_numbers = "".join(numbers_array)
		
		# Length validation
		length = len(extracted_numbers)
		if length < 10 or length > 11:
			raise ValueError("Must be 10 or 11 digits!")
		if length == 11:
			if extracted_numbers[0] != "1":
				raise ValueError("Country code must be 1!")
			# We don't need country code 1
			extracted_numbers = extracted_numbers[1:]

		self.area_code = extracted_numbers[0:3]
		self.exchange_code = extracted_numbers[3:6]
		self.subscriber_number = extracted_numbers[6:]
		
		# Validate codes
		if not self.__is_valid_area_code(self.area_code):
			raise ValueError("First digit of area code must be >= 2!")
		if not self.__is_valid_exchange_code(self.exchange_code):
			raise ValueError("First digit of exchange code must be >= 2!")
		
		self.number = f"{self.area_code}{self.exchange_code}{self.subscriber_number}"
		
	def pretty(self) -> str:
		return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
		
	def __is_valid_area_code(self, area_code: str) -> bool:
		return int(area_code[0]) >= 2
		
	def __is_valid_exchange_code(self, exchange_code: str) -> bool:
		return int(exchange_code[0]) >= 2
