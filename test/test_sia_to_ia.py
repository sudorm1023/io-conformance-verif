"""
该模块用来测试是否可以正常将*.si 文件中ia表示装换为InterfaceAutomata表示
"""

import unittest
import parserlib


class MyTestCase(unittest.TestCase):
    def test_testcase1(self):
        ia_rep = parserlib.read_si("../testcase_examples/testcase1.si")
        ia = parserlib.ia_parser(ia_rep)
        self.assertEqual(True, True)

    def test_testcase2(self):
        ia_rep = parserlib.read_si("../testcase_examples/testcase2.si")
        ia = parserlib.ia_parser(ia_rep)
        self.assertEqual(True, True)

    def test_testcase3(self):
        ia_rep = parserlib.read_si("../testcase_examples/testcase3.si")
        ia = parserlib.ia_parser(ia_rep)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

