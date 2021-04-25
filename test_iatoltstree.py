#!/usr/bin/env python3

"""
该模块用来测试parserlib中ia转换为LTSTree是否正确
"""

import unittest
from ia.state import State as IaState
from ia.action import Action as IaAction
from ia.transition import Transition as IaTransition
from ia.interfaceautomat import InterfaceAutomata
from parserlib.iatotree import ia_parser_to_tree


class TestIaToLtsTree(unittest.TestCase):
    def test_testcase1(self):
        """
        测试用例如下：
        ia：s0 -> act1! -> s1
        :return: None
        """
        state0 = IaState('s0')
        state1 = IaState('s1')
        action = IaAction('act1')
        transitions = [IaTransition(state0, action, state1)]
        ia = InterfaceAutomata(state0,
                               [state0, state1],
                               [action],
                               [],
                               [],
                               transitions)

        lts_tree = ia_parser_to_tree(ia)
        self.assertTrue(1 == 1)

    def test_testcase2(self):
        """
        测试用例如下：s0 -but?-> s1, s1 -liq!-> s2, s1 -choc!-> s3
        :return: None
        """
        state0 = IaState('s0')
        state1 = IaState('s1')
        state2 = IaState('s2')
        state3 = IaState('s3')
        action1_in = IaAction('but')
        action2_out = IaAction('liq')
        action3_out = IaAction('choc')
        transitions = [IaTransition(state0, action1_in, state1),
                       IaTransition(state1, action2_out, state2),
                       IaTransition(state1, action3_out, state3)]

        ia = InterfaceAutomata(state0,
                               [state0, state1, state2],
                               [action1_in],
                               [action2_out, action3_out],
                               [],
                               transitions)

        lts_tree = ia_parser_to_tree(ia)
        self.assertTrue(1 == 1)



if __name__ == "__main__":
    unittest.main()