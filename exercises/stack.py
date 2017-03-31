

class Stack:

    def __init__(self, *args):
        self.data = list(args)

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if self.data:
            return self.data[-1]
        return None

    def is_empty(self):
        return not bool(self.data)

    def _format_data_rep(self, limit=10):
        if self.data:
            datastr = " " + str(self.data[:limit])
            if len(self.data) > limit:
                datastr = datastr.rstrip(']')
                datastr += " ...]"
            return datastr
        return ""

    def __repr__(self):
        return "Stack {%d}%s" % (len(self.data), self._format_data_rep())


