ALLERGENS = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]

class Allergies:

	def __init__(self, score):
		self.allergies = [allergen for index, allergen in enumerate(ALLERGENS) if score & (1<<index)]

	def allergic_to(self, item):
		return item in self.allergies

	@property
	def lst(self):
		return self.allergies
