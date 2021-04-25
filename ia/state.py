#!/usr/bin/env python3

class State:
    """
    class State describe the abstraction of IA's state
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
