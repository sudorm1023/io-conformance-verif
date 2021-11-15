#!/usr/bin/env python3

"""
该模块用来描述安全迁移系统
"""

from typing import List

from ts import IOTS
from core import State
from core import Action
from core import Transition


class STS(IOTS):
    """
    类STS用来描述安全迁移系统
    """

    def __init__(self,
                 init_state: State,
                 states: List[State],
                 acts: List[Action],
                 ins: List[Action],
                 outs: List[Action],
                 transitions: List[Transition],
                 secure_level: dict
                 ):
        """
        :param init_state: The initialize state of IOTS
        :param states: The list of State
        :param acts: The list of all actions
        :param ins: The list of all input actions
        :param outs: The list of all output actions
        :param transitions: The list of transitions
        :param secure_level : 可观察动作到安全级别0或者1的一个映射
        """
        IOTS.__init__(init_state, states, acts, ins, outs, transitions)
        self.__secure_level = secure_level

    @property
    def secure_level(self):
        """
        :return: 可观察动作到安全级别0或者1的一个映射
        """
        return self.__secure_level

    @secure_level.setter
    def verdict(self, secure_level):
        self.__secure_level = secure_level

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

        secure_level = dict()
        for key, value in self.__secure_level:
            secure_level[key.action_name] = value

        return result + "{" + "\n\tstates: {},\n\tactions: {},\n\tinput actions: {},\n\toutput actions: {},\n\ttransitions: {}\n, secure level: {}\n".format(
            str(states),
            str(actions),
            str(input_actions),
            str(output_actions),
            str(transitions),
            str(secure_level)) + "}"

    def __str__(self):
        return self.__repr__()

