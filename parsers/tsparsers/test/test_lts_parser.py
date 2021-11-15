import unittest

from parsers.tsparsers import iots_parser


class MyTestCase(unittest.TestCase):
    def test_lts_parser(self):
        lts = iots_parser("./testcase_examples/testcase1.si")
        print(lts)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
