"""
Simple game of '21'
player gets 2 cards and then either sticks or twists until they have a score or go bust

"""
from enum import Enum
from random import shuffle

LIMIT = 21

LABELS = {
	1: "Ace",
	11: "Jack",
	12: "Queen",
	13: "King"  
}

class Suit(Enum):
     Clubs = 1
     Hearts = 2
     Spades = 3
     Diamonds = 4


class Game:
	pass


class Deck:

	@staticmethod
	def _create_cards():
		cards = []
		for s in Suit:
			for x in range(1, 14):
				cards.append(Card(s, x))
		return cards

	def __init__(self):
		self.cards = self._create_cards()

	def deal_card(self):
		return self.cards.pop()

	def shuffle_cards(self):
		shuffle(self.cards)


class Hand:

	def __init__(self):
		self.cards = []

	def add_card(self, card):
		self.cards.append(card)

	def score(self):
		"""
		a score of 0 means player is bust
		"""
		for score in self.scores():
			if score <= LIMIT:
				return score
		return 0

	def scores(self):
		score = 0
		has_ace = False
		for card in self.cards:
			score = score + card.value
			if card.value == 1:
				has_ace = True
		if has_ace:
			return [score + 10, score]
		return [score]


class Card:

	@property
	def name(self):
		return "{} of {}".format(LABELS.get(self.value, self.value), self.suit.name)

	def __init__(self, suit, value):
		if type(value) is not int:
			raise TypeError("Card value must be an integer")
		self.suit = suit
		self.value = value