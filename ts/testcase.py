#!/usr/bin/env python3

"""
该模块用用来表示一致性测试种testcase，它也是一种输入输出迁移系统
"""

from typing import List

from ts import IOTS
from core import Action
from core import State
from core import Transition


class Testcase(IOTS):
    """
    类Testcase表示一致性测试过程中测试用例对象
    """

    def __init__(self,
                 init_state: State,
                 states: List[State],
                 acts: List[Action],
                 ins: List[Action],
                 outs: List[Action],
                 transitions: List[Transition],
                 verdict: dict
                 ):
        """
        :param init_state: The initialize state of IOTS
        :param states: The list of State
        :param acts: The list of all actions
        :param ins: The list of all input actions
        :param outs: The list of all output actions
        :param transitions: The list of transitions
        :param verdict : 每个状态到pass(1)或者fail(0)的映射关系
        """
        IOTS.__init__(init_state, states, acts, ins, outs, transitions)
        self.__verdict = verdict

    @property
    def verdict(self):
        """
        :return: 返回testcase中状态到pass或者fail的映射关系的集合
        """
        return self.__verdict

    @verdict.setter
    def verdict(self, verdict):
        self.__verdict = verdict

    def __repr__(self):
        """
        格式化输出对象
        :return: str
        """
        result = ""
        result += self.__init_state.state_name

        states = [s.state_name for s in self.__states]
        actions = [a.action_name for a in self.__actions]

        input_actions = [a.action_name for a in self.input_actions]
        output_actions = [a.action_name for a in self.output_actions]
        transitions = [(t.start_state.state_name, t.action.action_name, t.end_state.state_name)
                       for t in self.__transitions]

        verdict = dict()
        for key, value in self.__verdict:
            result = "pass" if value else "fail"
            verdict[key.state_name] = result

        return result + "{" + "\n\tstates: {},\n\tactions: {},\n\tinput actions: {},\n\toutput actions: {},\n\ttransitions: {}\n, verdict: {}\n".format(
            str(states),
            str(actions),
            str(input_actions),
            str(output_actions),
            str(transitions),
            str(verdict)) + "}"

    def __str__(self):
        return self.__repr__()
