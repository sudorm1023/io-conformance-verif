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
        :param verdict : 每个状态到pass或者fail的映射关系
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
