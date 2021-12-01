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
        hide_acts = [a for a in acts if a not in (ins + outs)]
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

    def __repr__(self):
        """
        格式化输出对象
        :return: str
        """
        result = ""
        result += self.init_state.state_name

        states = [s.state_name for s in self.states]
        actions = [a.action_name for a in self.actions]

        input_actions = [a.action_name for a in self.input_actions]
        output_actions = [a.action_name for a in self.output_actions]
        transitions = [(t.start_state.state_name, t.action.action_name, t.end_state.state_name)
                       for t in self.transitions]

        return result + "{" + "\n\tstates: {},\n\tactions: {},\n\tinput actions: {},\n\toutput actions: {},\n\ttransitions: {}\n".format(
            str(states),
            str(actions),
            str(input_actions),
            str(output_actions),
            str(transitions)) + "}"

    def __str__(self):
        return self.__repr__()

