import unittest
from exercises.oop.blackjack import Card, Suit

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