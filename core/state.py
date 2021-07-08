#!/usr/bin/env python3

class State:
    """
    该类是对迁移系统种的State的抽象描述
    """

    def __init__(self, state_name: str):
        """
        :param state_name: the name of state
        """
        self.__state_name = state_name

    @property
    def state_name(self) -> str:
        return self.__state_name

    @state_name.setter
    def state_name(self, state_name: str):
        """
        :param state_name: The name of state
        :return: None
        """
        self.__state_name = state_name
