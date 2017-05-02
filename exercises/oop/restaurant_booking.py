
from datetime import datetime, date, time


class Restaurant:

	# opening_times is a list, 0 = Monday, 6 = Sunday
	# members are an oredered list of OPeningTime instances

	def __init__(self, name, tables=None):
		self.name = name
		self.tables = self._create_tables(tables)
		self.opening_times = []
		self.reservations = {}

	def retrieve_reservations(self, date, people=None):
		"""
		returns a list, ordered by table size (lo to hi), of reservations
		{
			table: [list of reservations]
		}
		we can limit what tables we return here
		"""
		return []

	def _is_table_free(table, reservations, time):
		"""
		:return: boolean
		"""


	def _create_tables(self, tables=None):
		if tables is None:
			return None
		return [Table(self, t) for t in sorted(tables)]

	def request_booking(self, customer, people, date, time):
		"""
		:param customer: Customer instance
		:param people: int
		:time: datetime
		returns: a Table instance or None
		"""

		# retrieve reservations for this day
		reservations = self.retrieve_reservations(date, people)

		# search for suitable tables
		# search for free slot on suitable tables
		# return free slot
		return None



class Table:

	def __init__(self, restaurant, seats):
		self.restaurant = restaurant
		self.seats = seats



class OpeningTime:
	restaurant
	day_of_week
	open
	close

	def set_open_time(self):
		self.open = time

	def set_close_time(self, time):
		self.close = time

	def delete(self):
		"""
		manages the restaurant relationship
		"""
		self.restaurant._delete_opening_time(self)


class Customer:
	name
	telephone


class Reservation:
	customer
	people
	date
	time
	duration




r = Restaurant(name="Cafe", tables=[4, 4, 4, 4, 4, 6, 6])
r.add_opening_time(day=0, open='1200', close='2359')
times = r.get_opening_times(day=0)
times[0].delete()

# what about opening on one day, closing the next? = 2 opening hours
# how do we handle multiple opening times in a single day?


c = Customer(name="Foo")

booking = r.request_booking(customer=c, people=4, time=datetime.now().replace(hours=19, minutes=0, seconds=0))

reservation = r.confirm_booking(booking)




