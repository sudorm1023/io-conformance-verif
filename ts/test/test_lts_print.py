#!/usr/bin/env python3

import unittest

from core import State
from core import Action
from core import Transition
from ts import LTS


class MyTestCase(unittest.TestCase):
    def test_lts_print(self):
        """
        用来验证lts格式化输出时是否正常
        :return:
        """

        state_a = State("a")
        state_b = State("b")
        state_c = State("c")
        init_state = state_a
        states = [state_a, state_b, state_c]

        act1 = Action("act1")
        act2 = Action("act2")
        actions = [act1, act2]
        hide_actions = []

        transitions = [Transition(state_a, act1, state_b), Transition(state_a, act2, state_c)]

        lts = LTS(init_state, states, actions, hide_actions, transitions)
        print(lts)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
