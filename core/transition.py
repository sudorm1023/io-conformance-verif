#!/usr/bin/env python3

from core import Action
from core import State


class Transition:
    """
    该类是迁移系统种Transition的抽象描述
    """

    def __init__(self, start_state: State, action: Action, end_state: State):
        """
        :param start_state: 转换的开始状态
        :param action: 转换上的动作
        :param end_state: 转换的结束状态
        """
        self.__start_state = start_state
        self.__action = action
        self.__end_start = end_state

    @property
    def start_state(self) -> State:
        return self.__start_state

    @start_state.setter
    def start_state(self, start_state: State):
        self.__start_state = start_state

    @property
    def action(self) -> Action:
        return self.__action

    @action.setter
    def action(self, action_: Action):
        self.__action = action_

    @property
    def end_state(self) -> State:
        return self.__end_start

    @end_state.setter
    def end_state(self, end_state: State):
        self.__end_start = end_state
