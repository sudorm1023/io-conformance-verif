import unittest

from lib.lts_tree import LTSTree
from lib.node import Node
from lib.state import State
from lib.action import Action
from lib.action import ActionEnum


class MyTestCase(unittest.TestCase):
    def test_init_p1(self):
        """
        implementation: s0 -but?-> s1, s1 -liq!-> s2
        :return:
        """
        imp_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("liq", ActionEnum.OUTPUT), State("s2"))
        imp_root.children = [node1]
        node1.children = [node2]
        imp = LTSTree(imp_root)
        results =imp.init_p()
        actions = [result[0] for result in results]
        self.assertTrue(actions == ['but'])

    def test_init_p2(self):
        """
        implementation：s0 -t-> s1, s1 -t-> s2, s2 -but?-> s3, s0 -lib!-> s4
        :return:
        """
        imp_root = Node(None, State("s0"))
        node1 = Node(Action("t", ActionEnum.INTERNAL), State("s1"))
        node2 = Node(Action("lib", ActionEnum.OUTPUT), State("s4"))
        imp_root.children = [node1, node2]
        node3 = Node(Action("t", ActionEnum.INTERNAL), State("s2"))
        node1.children = [node3]
        node4 = Node(Action("but", ActionEnum.INPUT), State("s3"))
        node3.children = [node4]
        imp = LTSTree(imp_root)
        results = imp.init_p()
        self.assertTrue(1 == 1, msg="True")


if __name__ == '__main__':
    unittest.main()
