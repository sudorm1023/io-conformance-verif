#!/usr/bin/env python3

"""
该模块是用来描述输入输出迁移系统（Input-Output Transition System， IOTS）
"""

from typing import List

from ts import LTS
from core import State
from core import Action
from core import Transition


class IOTS(LTS):
    """
    类IOTS用来表示输入输出迁移系统
    """

    def __init__(self,
                 init_state: State,
                 states: List[State],
                 acts: List[Action],
                 ins: List[Action],
                 outs: List[Action],
                 transitions: List[Transition]):
        """
        :param init_state: The initialize state of IOTS
        :param states: The list of State
        :param acts: The list of all actions
        :param ins: The list of all input actions
        :param outs: The list of all output actions
        :param transitions: The list of transitions
        """
        hide_acts = acts - ins - outs
        LTS.__init__(self, init_state, states, acts, hide_acts, transitions)
        self.__input_actions = ins
        self.__output_actions = outs

    @property
    def input_actions(self):
        """
        return: 返回所有输入动作对象的集合
        """
        return self.__input_actions

    @input_actions.setter
    def input_actions(self, ins: List[Action]):
        """
        :param ins: 待更新输入动作对象的集合
        """
        self.__input_actions = ins

    @property
    def output_actions(self):
        """
        return: 返回所有输出动作对象的集合
        """
        return self.__output_actions

    @output_actions.setter
    def output_actions(self, outs: List[Action]):
        """
        :param outs: 待更新输出动作对象的集合
        """
        self.__output_actions = outs

