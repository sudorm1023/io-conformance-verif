import unittest
from iparser import iparse


class TestIparser(unittest.TestCase):
    def test_iparse(self):
        iparse("../../testcase_examples/testcase1.si")
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
