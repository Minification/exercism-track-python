from math import floor
import random

def modifier(constitution):
	return floor((constitution - 10) / 2)

class Character:
	def __init__(self):
		for ab in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
			setattr(self, ab, self.ability())
		self.hitpoints = 10 + modifier(self.constitution)


	def ability(self):
		dice = random.sample(range(1, 7), 4)
		return sum(sorted(dice)[1:4])
