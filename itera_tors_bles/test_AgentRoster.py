import unittest
from AgentRoster import AgentRoster

class TestAgentRoster(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.roster = AgentRoster()

        self.roster.add_agent("Ann Tickwitee", 2539634)
        self.roster.add_agent("Ivan Idea", 1324595)
        self.roster.add_agent("Rock Solid", 1385723)
        self.roster.add_agent("Chase Devineaux", 1495263, True)

    def test_impl(self):
        for number, name in self.roster:
            print(f'{name}, id #{number}')

    def test_expl(self):

        # Get the iterator that is positioned that points to the iterable
        iter_ = iter(self.roster)
        while True:
            try:
                # Try to get the next item of the iterable
                agent = next(iter_)
                print(agent)
            except StopIteration:
                break
    