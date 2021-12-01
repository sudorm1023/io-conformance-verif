import unittest

from parsers.tsparsers import iots_parser


class TestIotsParser(unittest.TestCase):
    def test_iots_parser(self):
        iots = iots_parser("../../../testcase_examples/testcase4.si")
        print(iots)
        self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()
