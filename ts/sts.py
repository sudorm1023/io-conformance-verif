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
