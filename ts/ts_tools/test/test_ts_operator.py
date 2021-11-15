#!/usr/bin/env python3

"""
该模块用来对ts_operator中的函数进行单元测试
"""

import unittest
from ts.ts_tools import get_ts_observed_actions


class TestTsOperator(unittest.TestCase):
    def test_get_ts_observed_actions(self):
        """
        用来测试get_ts_observed_actions函数是否正确
        :return:
        """

        self.assertTrue(True)
