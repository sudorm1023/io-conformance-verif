#!/usr/bin/env python3

class Action:
    """
    该类是对Interface Automata中action的描述
    """

    def __init__(self, action_name: str):
        """
        :param action_name: the name of action
        """
        self.__name = action_name

    @property
    def action_name(self) -> str:
        """
        :return: the name of action
        """
        return self.__name

    @action_name.setter
    def action_name(self, action_name: str):
        self.__name = action_name
