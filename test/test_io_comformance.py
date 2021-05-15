#!/usr/bin/env python3

import unittest
from lib.lts_tree import LTSTree
from lib.node import Node
from lib.state import State
from lib.action import Action
from lib.action import ActionEnum


class TestIoConformation(unittest.TestCase):

    def test_testcase1(self):
        """
        测试用例如下：
        implementation：s0 -act1?-> s1
        specification: s0 -act1?-> s1
        :return: None
        """
        imp_root = Node(None, State("s0"))
        imp_root.children = [Node(Action("act1", ActionEnum.INPUT), State("s1"))]
        spec_root = Node(None, State("s0"))
        spec_root.children = [Node(Action("act1", ActionEnum.INPUT), State("s1"))]
        imp = LTSTree(imp_root)
        spec = LTSTree(spec_root)
        self.assertTrue(imp.io_conform(spec), msg="io not conform")

    def test_testcase2(self):
        """
        测试用例如下：
        implementation: s0 -but?-> s1, s1 -liq!-> s2
        specification: s0 -but?-> s1, s1 -liq!-> s2, s1 -choc-> s3
        :return: None
        """
        # implementation
        imp_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("liq", ActionEnum.OUTPUT), State("s2"))
        imp_root.children = [node1]
        node1.children = [node2]
        imp = LTSTree(imp_root)

        # specification
        spec_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("liq", ActionEnum.OUTPUT), State("s2"))
        node3 = Node(Action("choc", ActionEnum.OUTPUT), State("s3"))
        spec_root.children = [node1]
        node1.children = [node2, node3]
        spec = LTSTree(spec_root)

        self.assertTrue(imp.io_conform(spec), msg="io not conform")

    def test_testcase3(self):
        """
        测试用例如下：
        implementation: s0 -but?-> s1, s1 -liq!-> s2, s1 -choc!-> s3
        specification: s0 -but?-> s1, s1 -liq!-> s2
        :return:
        """
        # implementation
        imp_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("liq", ActionEnum.OUTPUT), State("s2"))
        node3 = Node(Action("choc", ActionEnum.OUTPUT), State("s3"))
        imp_root.children = [node1]
        node1.children = [node2, node3]
        imp = LTSTree(imp_root)

        # specification
        spec_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("liq", ActionEnum.OUTPUT), State("s2"))
        spec_root.children = [node1]
        node1.children = [node2]
        spec = LTSTree(spec_root)

        self.assertFalse(imp.io_conform(spec), msg="Error, test result: io conform!")

    def test_testcase4(self):
        """
        测试用例如下：
        implementation: s0 -but?-> s1, s1 -liq!-> s2
        specification: s0 -but?-> s1, s0 -but?-> s2, s1 -liq!-> s3, s2 -but?-> s4, s4 -choc!-> s5
        :return: None
        """
        # implementation
        imp_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("liq", ActionEnum.OUTPUT), State("s2"))
        imp_root.children = [node1]
        node1.children = [node2]
        imp = LTSTree(imp_root)

        # specification
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

        self.assertFalse(imp.io_conform(spec), msg="Error, test result: io conform!")

    def test_testcase5(self):
        """
        测试用例如下：
        implementation: s0 -but?-> s1, s1 -liq!-> s2, s1 -choc!-> s3
        specification: s0 -but?-> s1, s0 -but?-> s2, s1 -liq!-> s3, s2 -but?-> s4, s4 -choc!-> s5
        :return: None
        """
        # implementation
        imp_root = Node(None, State("s0"))
        node1 = Node(Action("but", ActionEnum.INPUT), State("s1"))
        node2 = Node(Action("liq", ActionEnum.OUTPUT), State("s2"))
        node3 = Node(Action("choc", ActionEnum.OUTPUT), State("s3"))
        imp_root.children = [node1]
        node1.children = [node2, node3]
        imp = LTSTree(imp_root)

        # specification
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

        self.assertFalse(imp.io_conform(spec), msg="Error, test result: io conform!")


if __name__ == "__main__":
    unittest.main()
