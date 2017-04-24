import unittest

from exercises.oop.networks import Village, Inhabitant

class TestVillage(unittest.TestCase):

	def test_initialisation(self):
		v = Village()
		self.assertEqual(v.inhabitants, [])

		v = Village(name="Netherthong")
		self.assertEqual(v.name, "Netherthong")

	def test_add_inhabitant(self):
		v = Village()
		i = Inhabitant()
		v.add_inhabitant(i)
		self.assertTrue(i in v.inhabitants)
		self.assertEqual(i.village, v)

	def test_get_most_connected(self):
	    v = Village()
	    for x in range(0, 5):
	        inhabitant = Inhabitant('Person %d' % x, v)
	        v.add_inhabitant(inhabitant)
	    # connect neighbours
	    v.inhabitants[0].connect(v.inhabitants[1])
	    v.inhabitants[1].connect(v.inhabitants[2])
	    v.inhabitants[2].connect(v.inhabitants[3])
	    v.inhabitants[3].connect(v.inhabitants[4])
	    self.assertEqual(v.get_most_connected(), v.inhabitants[1:-1])
	    # now, connect last one to first & second
	    v.inhabitants[4].connect(v.inhabitants[0])
	    v.inhabitants[4].connect(v.inhabitants[1])
	    v.inhabitants[4].connect(v.inhabitants[2])
	    self.assertEqual(v.get_most_connected(), [v.inhabitants[4]])


class TestInhabitant(unittest.TestCase):

	def test_connect(self):
		carl = Inhabitant(name="Carl")
		lenny = Inhabitant(name="Lenny")
		carl.connect(lenny)
		self.assertEqual(carl.connection_count, 1)
		self.assertEqual(lenny.connection_count, 1)
		self.assertTrue(carl.connected_to(lenny))
		self.assertTrue(lenny.connected_to(carl))

	def test_not_connected(self):
		loki = Inhabitant(name="Loki")
		thor = Inhabitant(name="Thor")
		hagrid = Inhabitant(name="Hagrid")
		loki.connect(hagrid)
		self.assertFalse(loki.connected_to(thor))

	def test_unconnect(self):
		carl = Inhabitant(name="Carl")
		lenny = Inhabitant(name="Lenny")
		carl.connect(lenny)
		self.assertTrue(carl.connected_to(lenny))
		carl.unconnect(lenny)
		self.assertEqual(carl.connection_count, 0)
		self.assertEqual(lenny.connection_count, 0)
		self.assertFalse(carl.connected_to(lenny))
		self.assertFalse(lenny.connected_to(carl))


class TestInhabitantConnector(unittest.TestCase):

	def setUp(self):
		self.alf = Inhabitant(name="Alf")
		self.bob = Inhabitant(name="Bob")
		self.alf.connect(self.bob)
		self.cal = Inhabitant(name="Cal")
		self.bob.connect(self.cal)
		self.don = Inhabitant(name="Don")
		self.cal.connect(self.don)
		self.egg = Inhabitant(name="Egbert")

	def test_direct_connection(self):
		connection = self.alf.find_connection_to(self.bob)
		self.assertEqual(connection, [self.alf, self.bob])

	def test_level2_connection(self):
		connection = self.alf.find_connection_to(self.cal)
		self.assertEqual(connection, [self.alf, self.bob, self.cal])

	def test_level3_connection(self):
		connection = self.alf.find_connection_to(self.don)
		self.assertEqual(connection, [self.alf, self.bob, self.cal, self.don])

	def test_level4_connection(self):
		connection = self.alf.find_connection_to(self.cal)
		self.assertEqual(connection, [self.alf, self.bob, self.cal])

	def test_no_connection(self):
		connection = self.alf.find_connection_to(self.egg)
		self.assertIsNone(connection, None)

	def test_a_loop_of_connections_is_handled(self):
		alpha = Inhabitant()
		bravo = Inhabitant()
		charlie = Inhabitant()
		delta = Inhabitant()

		alpha.connect(bravo)
		bravo.connect(charlie)
		charlie.connect(delta)
		delta.connect(bravo)

		connection = alpha.find_connection_to(bravo)
		self.assertEqual(connection, [alpha, bravo])


