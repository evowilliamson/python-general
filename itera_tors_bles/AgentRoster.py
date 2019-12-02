class AgentRoster:

    def __init__(self):
        self._agents = {}
        self._classified = []

    def add_agent(self, name, number, classified=False):
        self._agents[number] = name
        if classified:
            self._classified.append(name)

    def validate_number(self, number):
        try:
            name = self._agents[number]
        except KeyError:
            return False
        else:
            return True

    def lookup_agent(self, number):
        try:
            name = self._agents[number]
        except KeyError:
            name = "<NO KNOWN AGENT>"
        else:
            if name in self._classified:
                name = "<CLASSIFIED>"
        return name

    def __iter__(self):
        """ AgentRoster is now an iterable, because __iter___ has been defined """
        return AgentRoster.AgentRoster_Iterator(self)


    class AgentRoster_Iterator:
        """ This is the iterator of AgentRoster """

        def __init__(self, container):
            self._roster = list(container._agents.items())
            self._classified = container._classified
            self._max = len(self._roster) - len(self._classified)
            self._index = 0        

        def __next__(self):
            """ It's a requirement for an iterator to have an __next__ method """
            if self._index == self._max:
                raise StopIteration
            else:
                r = self._roster[self._index]
                self._index += 1
                return r            

