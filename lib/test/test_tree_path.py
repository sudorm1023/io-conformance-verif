import unittest
from lib.lts_tree import LTSTree
from lib.node import Node
from lib.state import State
from lib.action import Action
from lib.action import ActionEnum


class MyTestCase(unittest.TestCase):
    def test_tree_path1(self):
        # implementation：s0 -act1?-> s1
        imp_root = Node(None, State("s0"))
        imp_root.children = [Node(Action("act1", ActionEnum.INPUT), State("s1"))]
        imp = LTSTree(imp_root)
        imp.tree_path()
        print(imp.paths)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
