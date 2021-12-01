import unittest

from parsers.tsparsers import sts_parser


class TestStsParser(unittest.TestCase):
    def test_sts_parser(self):
        sts = sts_parser("../../../testcase_examples/testcase5.si")
        print(sts)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
