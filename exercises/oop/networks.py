"""
Problem
The inhabitants of a village are represented, along with their connections. Find the person in the village with the highest number of friends.
"""

class Village:

    def __init__(self, name=None):
        self.inhabitants = []
        self.name = name or "Anonymous Village"

    def add_inhabitant(self, inhabitant):
        inhabitant.village = self
        self.inhabitants.append(inhabitant)

    def get_most_connected(self):
        inhabitants = {}
        for inhabit in self.inhabitants:
            i = inhabitants.get(inhabit.connection_count, [])
            i.append(inhabit)
            inhabitants[inhabit.connection_count] = i
        keys = inhabitants.keys()
        if not keys:
            return None
        keys = sorted(keys)
        keys.reverse()
        return inhabitants[keys[0]]


class Inhabitant:

    def __init__(self, name=None, village=None):
        self.name = name or "Anonymous"
        self.village = village
        self.connection_count = 0
        self.connections = []

    def unconnect(self, inhabitant):
        """
        connect two inhabitants
        """
        self._remove_connection(inhabitant)
        inhabitant._remove_connection(self)

    def _remove_connection(self, inhabitant):
        """
        connect two inhabitants
        """
        self.connections = filter(lambda x: x != inhabitant, self.connections)
        self.connection_count -= 1

    def connect(self, inhabitant):
        """
        connect two inhabitants
        """
#        connection = Connection(self, inhabitant)
        #TODO - do we need this connection? If so, should we store a reference to it?
        self._add_connection(inhabitant)
        inhabitant._add_connection(self)

    def _add_connection(self, inhabitant):
        self.connection_count += 1
        self.connections.append(inhabitant)

    def connected_to(self, inhabitant):
        """
        returns True if this Inhabitant is connected to the 
        inhabitant argument
        :param inhabitant: Inhabitant instance
        :returns: boolean
        """
        return inhabitant in self.connections

    def find_connection_to(self, inhabitant):
        # build larger and larger connection maps from each inhabitant
        # the moment we find an overlap between the sets of inhabitants
        # is the moment we have a full path :)
        return []

    def build_connection_map(self, inhabitant):
        """
        returns a list of inhabitants who are connected, starts with self, ends with inhabitant
        it should be the shortest possible chain
        """

        # technique here is to do a breadth-first search
        # from both inhabitants, once we find a common connection, we stitch the two paths together
        connection_map = {}
        for inhab in self.connections:
            connection_map[inhab] = [inhab]
        # recursive loop - needs a sane limit one would think...
        for val in connection_map.values():
            final_chain = val[-1]
            for inhab in final_chain.connections:
                if inhab not in connection_map.keys():
                    connection_map[inhab] = val + [inhab]
        self.connection_map = connection_map


    def __repr__(self):
        return "<{} ({})>".format(self.name, self.connection_count)

