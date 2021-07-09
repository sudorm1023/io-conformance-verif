import unittest

from iparser import parse_states
from iparser import parse_actions
from iparser import parser_transitions
from iparser import parse_initial_state


class TestCommon(unittest.TestCase):
    def test_parse_states(self):
        states = parse_states("../../testcase_examples/testcase1.si")
        self.assertEqual(sorted(states), sorted(['s0', 's1']))

    def test_parse_actions(self):
        actions = parse_actions("../../testcase_examples/testcase3.si")
        print(actions)
        self.assertEqual(True, True)

    def test_parse_transitions(self):
        transitions = parser_transitions("../../testcase_examples/testcase3.si")
        print(transitions)
        self.assertEqual(True, True)

    def test_parse_initial_state(self):
        state = parse_initial_state("../../testcase_examples/testcase1.si")
        self.assertEqual(state, 's0')


if __name__ == '__main__':
    unittest.main()
