"""
Simple game of '21'
player gets 2 cards and then either sticks or twists until they have a score or go bust

"""
from enum import Enum

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

	def __init__():
		self.cards = []


class Hand:
	pass


class Card:

	@property
	def name(self):
		return "{} of {}".format(LABELS.get(self.value, self.value), self.suit.name)

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value