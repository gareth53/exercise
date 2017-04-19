import unittest
from copy import copy
from exercises.oop.blackjack import Card, Suit, Deck, Hand, Game


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

	def test_value(self):
		card = Card(Suit.Diamonds, 1)
		self.assertEqual(card.value, 1)
		
		card = Card(Suit.Hearts, 2)
		self.assertEqual(card.value, 2)

		card = Card(Suit.Hearts, 11)
		self.assertEqual(card.value, 10)		

		card = Card(Suit.Spades, 12)
		self.assertEqual(card.value, 10)
		
		card = Card(Suit.Clubs, 13)
		self.assertEqual(card.value, 10)


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


class TestHandScoring(unittest.TestCase):

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


class TestHandDescribe(unittest.TestCase):

	def test_simple(self):
		hand = Hand()
		hand.add_card(Card(Suit.Clubs, 2))
		hand.add_card(Card(Suit.Clubs, 10))
		self.assertEqual(hand.describe_hand(), "2 of Clubs, 10 of Clubs")

	def test_fivecard_score(self):
		hand = Hand()
		hand.add_card(Card(Suit.Clubs, 2))
		hand.add_card(Card(Suit.Diamonds, 2))
		hand.add_card(Card(Suit.Spades, 2))
		hand.add_card(Card(Suit.Hearts, 2))
		hand.add_card(Card(Suit.Hearts, 5))
		self.assertEqual(hand.describe_hand(), "2 of Clubs, 2 of Diamonds, 2 of Spades, 2 of Hearts, 5 of Hearts")


class TestHandStickOrTwist(unittest.TestCase):

	def test_first_twist(self):
		game = Game()
		hand = Hand(game=game)
		hand.add_card(Card(Suit.Diamonds, 2))
		hand.add_card(Card(Suit.Hearts, 2))
		game.hands = [hand]

		hand.stick_or_twist()
		self.assertFalse(hand.completed)
		self.assertEqual(len(hand.cards), 3)

	def test_borderline_twist(self):
		game = Game()
		hand = Hand(game=game)
		hand.add_card(Card(Suit.Diamonds, 10))
		hand.add_card(Card(Suit.Hearts, 6))
		game.hands = [hand]

		hand.stick_or_twist()
		self.assertFalse(hand.completed)
		self.assertEqual(len(hand.cards), 3)

	def test_stick(self):
		game = Game()
		hand = Hand(game=game)
		hand.add_card(Card(Suit.Diamonds, 10))
		hand.add_card(Card(Suit.Hearts, 7))
		game.hands = [hand]

		hand.stick_or_twist()
		self.assertTrue(hand.completed)


class TestGame(unittest.TestCase):

	def test_deal(self):
		g = Game()
		g._deal()
		for hand in g.hands:
			self.assertEqual(len(hand.cards), 2)
			self.assertEqual(type(hand), Hand)

	def test_get_scores(self):
		g = Game()

		h1 = Hand(player_name="Henry")
		h1.add_card(Card(Suit.Diamonds, 2))
		h1.add_card(Card(Suit.Diamonds, 3))
		h2 = Hand(player_name="Steve")
		h2.add_card(Card(Suit.Clubs, 10))
		h2.add_card(Card(Suit.Spades, 11))
		h3 = Hand(player_name="Gregg")
		h3.add_card(Card(Suit.Spades, 10))
		h3.add_card(Card(Suit.Diamonds, 11))
		h3.add_card(Card(Suit.Spades, 12))

		g.hands = [h1, h2, h3]
		scores = g._get_scores()
		self.assertEqual(len(scores), 3)

		self.assertEqual(scores[0], "Henry scored 5")
		self.assertEqual(scores[0], "Steve scored 21")
		self.assertEqual(scores[0], "Gregg 3 went bust :(")


	def test_get_winning_hands(self):
		assert False

	def test_announce_result(self):
		assert False
