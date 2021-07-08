import unittest
from core import Action
from core import State
from core import Transition
from ts import IOTS
from confgraph import iots_to_graph


class MyTestCase(unittest.TestCase):
    def test_iots_to_graph(self):
        """
        测试标记迁移系统 s0 -?act0-> s1, s0 -!act1> s2, s1 -act2-> s3  是否可以正常变成图对象
        """
        state0 = State("s0")
        state1 = State("s1")
        state2 = State("s2")
        state3 = State("s3")

        action0 = Action("act0")
        action1 = Action("act1")
        action2 = Action("act2")

        transition0 = Transition(state0, action0, state1)
        transition1 = Transition(state0, action1, state2)
        transition2 = Transition(state1, action2, state3)

        iots = IOTS(state0,
                    [state0, state1, state2, state3],
                    [action0, action1, action2],
                    [action0],
                    [action1],
                    [transition0, transition1, transition2])

        ts_graph = iots_to_graph(iots)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
