import unittest
from lib.lts_tree import LTSTree
from lib.node import Node
from lib.state import State
from lib.action import Action
from lib.action import ActionEnum
from lib.lts_tree import get_quiescent_states


class MyTestCase(unittest.TestCase):
    def test_get_quiescent_states(self):
        # implementation
        imp_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("liq", ActionEnum.OUTPUT), State("s2"))
        imp_root.children = [node1]
        node1.children = [node2]
        imp = LTSTree(imp_root)
        states = get_quiescent_states(imp)
        self.assertEqual([state.state_name for state in states], ['s1'])

    def test_get_quiescent_stetes1(self):
        # specification
        # specification: s0 - but?-> s1, s0 - but?-> s2, s1 - liq!-> s3, s2 - but?-> s4, s4 - choc!-> s5
        spec_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("but", ActionEnum.INPUT), State("s2"))
        spec_root.children = [node1, node2]
        node3 = Node(Action("liq", ActionEnum.OUTPUT), State("s3"))
        node1.children = [node3]
        node4 = Node(Action("but", ActionEnum.INPUT), State("s4"))
        node2.children = [node4]
        node5 = Node(Action("liq", ActionEnum.OUTPUT), State("s5"))
        node4.children = [node5]
        spec = LTSTree(spec_root)
        states = get_quiescent_states(spec)
        self.assertEqual([state.state_name for state in states], ['s1', 's4'])


if __name__ == '__main__':
    unittest.main()
