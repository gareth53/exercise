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

    def get_connection_map(self, chain=None):
        if not chain:
            chain = [self]
        connection_map = {inhab: chain + [inhab] for inhab in self.connections}
        self.connection_map = connection_map
        return connection_map

    def find_connection_to(self, inhabitant, recursion_limit=4):
        """
        returns a list of inhabitants who are connected, starts with self, ends with inhabitant
        it should be the shortest possible chain
        """
        # technique here is to do a breadth-first search
        # from both inhabitants, once we find a common connection, we stitch the two paths together
        if self.connected_to(inhabitant):
            return [self, inhabitant]
        self.get_connection_map()
        inhabitant.get_connection_map()

        for x in range(0, recursion_limit):
            self.add_layer_to_connections_map()
            inhabitant.add_layer_to_connections_map()

            overlap = self.find_connection(self, inhabitant)
            if overlap:
                return self.build_connection_path(overlap.pop(), inhabitant)
        return None

    def build_connection_path(self, connector, inhabitant):
        """
        since we're calling this method we assume that the connector is a key
        that is common to both inhabitant's connection_maps
        """
        path_start = self.connection_map[connector][:-1]
        path_end = inhabitant.connection_map[connector]
        path_end.reverse()
        return path_start + path_end

    @staticmethod
    def find_connection(inhabitant1, inhabitant2):
        i1 = set(inhabitant1.connection_map.keys())
        i2 = set(inhabitant2.connection_map.keys())
        return i1.intersection(i2)

    def add_layer_to_connections_map(self):
        """
        grows the connections by one layer
        i.e. adds the contacts of contacts
        """
        new_connections = {}
        for val in self.connection_map.values():
            final_chain = val[-1]
            connections_to_add = final_chain.get_connection_map(chain=val)
            new_connections.update(connections_to_add)
        # now knit the new connections into the connection_map
        for key, val in new_connections.items():
            if key not in self.connection_map and key != self:
                self.connection_map[key] = val

    def __repr__(self):
        return "<{}>".format(self.name, self.connection_count)

