#!/usr/bin/env python3


"""
该模块用来表示标记迁移系统(Labeled Transition System, LTS)
"""
from typing import List

from core import State
from core import Action
from core import Transition


class LTS:
    """
    类LTS描述标记迁系统
    """
    def __init__(self,
                 init_state: State,
                 states: List[State],
                 acts: List[Action],
                 hide_acts: List[Action],
                 transitions: List[Transition]):
        """
        :param init_state: The initialize state of IA
        :param states: The list of State
        :param acts: The list of all actions
        :param hide_acts: The list of all unobserved actions
        :param transitions: The list of transitions
        """
        self.__init_state = init_state
        self.__states = states
        self.__actions = acts
        self.__hide_actions = hide_acts
        self.__transitions = transitions

    @property
    def states(self) -> List[State]:
        """
        :return: 返回LTS中所有状态对象的集合
        """
        return self.__states

    @states.setter
    def states(self, states: List[State]):
        """
        :param states: 更新状态集合
        """
        self.__states = states

    def add_state(self, state):
        """
        :param state: 增加状态
        """
        if isinstance(state, list):
            self.__states.extend(state)
        else:
            self.__states.append(state)

    @property
    def transitions(self) -> List[Transition]:
        """
        :return: 返回所有Transition对象集合
        """
        return self.__transitions

    @transitions.setter
    def transitions(self, trans: List[Transition]):
        """
        :param trans: 更新Transition对象的集合
        """
        self.__transitions = trans

    def add_transition(self, tran):
        """
        增加一个Transition对象或者一组Transition对象
        :param tran: 需要增加的Transition对象
        """
        if isinstance(tran, list):
            self.__transitions.extend(tran)
        else:
            self.__transitions.append(tran)

    @property
    def init_state(self):
        """
        :return: The initial state of LTS
        """
        return self.__init_state

    @init_state.setter
    def init_state(self, state: State):
        """
        :param state: Update new initial state
        :return: None
        """
        self.__init_state = state

    @property
    def actions(self):
        """
        :return: 返回所有动作对象
        """
        return self.__actions

    @actions.setter
    def actions(self, acts):
        self.__actions = acts

    @property
    def hide_actions(self):
        """
        :return: 返回不可观察对象
        """
        return self.__hide_actions

    @hide_actions.setter
    def hide_actions(self, hide_acts):
        self.__hide_actions = hide_acts

