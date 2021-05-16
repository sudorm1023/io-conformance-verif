import unittest
from parserlib import read_si
from parserlib import ia_parser
from parserlib import ia_parser_to_tree


class MyTestCase(unittest.TestCase):
    def test_testcase4(self):
        ia_rep_spec = read_si("./testcase_examples/testcase4_imp.si")
        ia_rep_imp = read_si("./testcase_examples/testcase4_imp.si")
        ia_spec = ia_parser(ia_rep_spec)
        ia_imp = ia_parser(ia_rep_imp)
        ia_spec_tree = ia_parser_to_tree(ia_spec)
        ia_imp_tree = ia_parser_to_tree(ia_imp)
        self.assertTrue(ia_imp_tree.io_conform(ia_spec_tree), msg="io not conform")

    def test_case5(self):
        ia_rep_spec = read_si("./testcase_examples/testcase5_imp.si")
        ia_rep_imp = read_si("./testcase_examples/testcase5_imp.si")
        ia_spec = ia_parser(ia_rep_spec)
        ia_imp = ia_parser(ia_rep_imp)
        ia_spec_tree = ia_parser_to_tree(ia_spec)
        ia_imp_tree = ia_parser_to_tree(ia_imp)
        self.assertTrue(ia_imp_tree.io_conform(ia_spec_tree), msg="io not conform")

    # have problem
    def test_case6(self):
        ia_rep_spec = read_si("./testcase_examples/testcase6_imp.si")
        ia_rep_imp = read_si("./testcase_examples/testcase6_imp.si")
        ia_spec = ia_parser(ia_rep_spec)
        ia_imp = ia_parser(ia_rep_imp)
        ia_spec_tree = ia_parser_to_tree(ia_spec)
        ia_imp_tree = ia_parser_to_tree(ia_imp)
        self.assertFalse(ia_imp_tree.io_conform(ia_spec_tree), msg="io not conform")

    def test_case7(self):
        ia_rep_spec = read_si("./testcase_examples/testcase7_imp.si")
        ia_rep_imp = read_si("./testcase_examples/testcase7_imp.si")
        ia_spec = ia_parser(ia_rep_spec)
        ia_imp = ia_parser(ia_rep_imp)
        ia_spec_tree = ia_parser_to_tree(ia_spec)
        ia_imp_tree = ia_parser_to_tree(ia_imp)
        self.assertTrue(ia_imp_tree.io_conform(ia_spec_tree), msg="io not conform")

    # have problem
    def test_case8(self):
        ia_rep_spec = read_si("./testcase_examples/testcase8_imp.si")
        ia_rep_imp = read_si("./testcase_examples/testcase8_imp.si")
        ia_spec = ia_parser(ia_rep_spec)
        ia_imp = ia_parser(ia_rep_imp)
        ia_spec_tree = ia_parser_to_tree(ia_spec)
        ia_imp_tree = ia_parser_to_tree(ia_imp)
        self.assertFalse(ia_imp_tree.io_conform(ia_spec_tree), msg="io not conform")


if __name__ == '__main__':
    unittest.main()
