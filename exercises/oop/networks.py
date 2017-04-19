"""
Problem
The inhabitants of a village are represented, along with their connections. Find the person in the village with the highest number of friends.
"""

class Village:

    inhabitants = []

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    def get_random_inhabitant(self):
        return self.inhabitants[math.random(len(self.inhabitantats)) - 1]

    def _get_most_connected(self, n=1):
        inhabitants = {}
        for inhabit in self.inhabitants:
            i = inhabitants.get(inhabit.connections_count, [])
            inhabitants[inhabit.connections_count] = i.append(inhabit)
        keys = inhabitants.keys()
        if not keys:
            return None
        keys = sorted(keys)
        keys.reverse()
        return inhabitants[keys[:n]]


class Inhabitant:
    name = ""
    village = village
    connection_count = 0
    connections = []

    def connect(self, inhabitant):
        connection = Connection(self, inhabitant)
        self.add_connection(connection)
        inhabitant.add_connection(connection)

    def add_connection(self, inhabitant):
        self.connnection_count += 1
        connection = Connection(self, inhabitant)
        self.connections.append(connection)


class Connection:
    
    def __init__(self, inhabitant1, inhabitant2):
        self.inhabitant1 = inhabitant1
        self.inhabitant2 = inhabitant2


def setup():
    v = Village()
    for x in range(0, 50):
        inhabitant = Inhabitant('Person %d' % x, v)
        v.add_inhabitant(inhabitant)
    for y in range(0, 300):
        inhabitant1 = v.get_random_inhabitant()
        inhabitant2 = v.get_random_inhabitant()
        inhabitant1.connect(inhabitant2)


def find_most_connected(village):





