import unittest

from parsers.tsparsers import lts_parser


class MyTestCase(unittest.TestCase):
    def test_lts_parser1(self):
        lts = lts_parser("../../../testcase_examples/testcase1.si")
        print(lts)
        self.assertEqual(True, True)

    def test_lts_parser2(self):
        lts = lts_parser("../../../testcase_examples/testcase2.si")
        print(lts)
        self.assertEqual(True, True)

    def test_lts_parser3(self):
        lts = lts_parser("../../../testcase_examples/testcase3.si")
        print(lts)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
