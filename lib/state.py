#!/usr/bin/env python3

class State:
    """
    类State是对 Labbled Transition System 中状态的抽象
    """

    def __init__(self, state_name: str):
        """
        构造函数
        :param state_name: 状态节点的标识名称
        :return: None
        """
        self.__name = state_name

    @property
    def state_name(self) -> str:
        """
        获取状态节点的标识名称
        :return: 节点的名称
        """
        return self.__name

    @state_name.setter
    def state_name(self, state_name: str):
        """
        更改节点的名称
        :param state_name: 新的节点名称
        :return: None
        """
        self.__name = state_name
