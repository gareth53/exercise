import unittest
from copy import copy
from exercises.oop.blackjack import Card, Suit, Deck, Hand


class TestCard(unittest.TestCase):

	def test_description(self):
		card = Card(Suit.Diamonds, 1)
		self.assertEqual(card.name, "Ace of Diamonds")
		
		card = Card(Suit.Hearts, 2)
		self.assertEqual(card.name, "2 of Hearts")

		card = Card(Suit.Hearts, 10)
		self.assertEqual(card.name, "10 of Hearts")		

		card = Card(Suit.Spades, 11)
		self.assertEqual(card.name, "Jack of Spades")
		
		card = Card(Suit.Clubs, 12)
		self.assertEqual(card.name, "Queen of Clubs")

		card = Card(Suit.Clubs, 13)
		self.assertEqual(card.name, "King of Clubs")


class TestDeck(unittest.TestCase):

	def test_create(self):
		deck = Deck()
		self.assertEqual(len(deck.cards), 52)

	def test_all_cards_have_unique_names(self):
		card_counter = set()
		deck = Deck()
		for card in deck.cards:
			card_counter.add(card.name)
		self.assertEqual(len(card_counter), 52)

	def test_shuffle(self):
		deck = Deck()
		for x in range(0, 5):
			pre_shuffle = copy(deck.cards)
			deck.shuffle_cards()
			self.assertNotEqual(pre_shuffle, deck.cards)

class TestHand(unittest.TestCase):

	def test_simple_score(self):
		hand = Hand()
		hand.add_card(Card(Suit.Clubs, 2))
		hand.add_card(Card(Suit.Clubs, 10))
		self.assertEqual(hand.score(), 12)

	def test_fivecard_score(self):
		hand = Hand()
		hand.add_card(Card(Suit.Clubs, 2))
		hand.add_card(Card(Suit.Diamonds, 2))
		hand.add_card(Card(Suit.Spades, 2))
		hand.add_card(Card(Suit.Hearts, 2))
		hand.add_card(Card(Suit.Hearts, 5))
		self.assertEqual(hand.score(), 13)

	def test_score_with_high_ace(self):
		hand = Hand()
		hand.add_card(Card(Suit.Hearts, 1))
		hand.add_card(Card(Suit.Hearts, 9))
		self.assertEqual(hand.score(), 20)

	def test_score_with_low_ace(self):
		hand = Hand()
		hand.add_card(Card(Suit.Hearts, 1))
		hand.add_card(Card(Suit.Hearts, 4))
		hand.add_card(Card(Suit.Hearts, 10))
		self.assertEqual(hand.score(), 15)
