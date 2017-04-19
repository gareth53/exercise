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

class GameError(Exception):
	pass

class Suit(Enum):
     Clubs = 1
     Hearts = 2
     Spades = 3
     Diamonds = 4


class Game:
	
	def __init__(self, players=2):
		self.deck = Deck()
		self.hands = [Hand(player_name="Player %d" % (x+1), game=self) for x in range(0, players)]

	def _deal(self):
		self.deck.shuffle_cards()
		for x in range(0, 2):
			for hand in self.hands:
				hand.add_card(self.deck.deal_card())

	def conduct_game(self):
		self._deal()
		for hand in self.hands:
			while hand.completed is not True:
				hand.stick_or_twist()
		self._complete_game()

	def _complete_game(self):
		for score in self._get_scores():
			print(score)
		print(self.announce_result())

	def _get_scores(self):
		scores = []
		for p in self.hands:
			name = p.player_name
			score = p.score()
			print("{} has {}".format(name, p.describe_hand()))
			if score == 0:
				scores.append("{} went bust :(".format(name))
			else:
				scores.append("{} scored {}".format(name, score))
		return scores

	def _get_winning_hands(self):
		# look through the hands, find highest score
		self.hands.sort(key=lambda x: x.score())
		winners = []
		last_score = None
		while self.hands:
			hand = self.hands.pop()
			if last_score and hand.score() < last_score:
				break
			last_score = hand.score()
			winners.append(hand)
		return winners

	def _announce_result(self):
		hands = self._get_winning_hands()
		if len(hands) > 1:
			return "TIE! {} all scored {}".format(", ".join([hand.player_name for hand in hands]), hands[0].score())
		return "{} WINS with a score of {}".format(hands[0].player_name, hands[0].score())


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

	def __init__(self, player_name=None, game=None):
		self.cards = []
		self.game = game
		self.player_name = player_name
		self.completed = False
		self._score = None

	def add_card(self, card):
		self._score = None
		self.cards.append(card)

	def describe_hand(self):
		cards = [card.name for card in self.cards]
		return ", ".join(cards)

	def score(self):
		"""
		a score of 0 means player is bust
		"""
		if self._score:
			return self._score
		for score in self._scores():
			if score <= LIMIT:
				return score
		return 0

	def _scores(self):
		score = 0
		has_ace = False
		for card in self.cards:
			score = score + card.value
			if card.value == 1:
				has_ace = True
		if has_ace:
			return [score + 10, score]
		return [score]

	def stick(self):
		self.completed = True

	def twist(self):
		if self.score() > 21:
			raise BustException("A player can't twist if he's already bust!")
		self.add_card(self.game.deck.deal_card())

	def stick_or_twist(self):
		"""
		if any score is > 16, stick...
		"""
		if sorted(self._scores())[-1] > 16:
			self.stick()
		else:
			self.twist()


class Card:

	@property
	def name(self):
		return "{} of {}".format(LABELS.get(self.identifier, self.identifier), self.suit.name)

	def __init__(self, suit, identifier):
		if type(identifier) is not int:
			raise TypeError("Card identifier must be an integer")
		self.suit = suit
		self.identifier = identifier
		self.value = identifier if identifier < 11 else 10


if __name__ == "__main__":
	game = Game(players=6)
	game.conduct_game()
