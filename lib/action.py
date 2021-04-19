#!/usr/bin/env python3

"""
该模块是是对LTS系统中动作进行抽象
"""

import enum


class ActionEnum(enum.Enum):
    """
    对LTS系统中Action进行区分：
    0 表示输入动作
    1 表示输出动作
    2 表示内部动作
    """
    INPUT = 0
    OUTPUT = 1
    INTERNAL = 2


class Action:
    """
    对LTS中动作进行抽象
    """
    def __init__(self, action_name: str, action_type: ActionEnum):
        """
        Action类的构造函数，LTS中的动作由名字和类型标识
        :param action_name:
        :param action_type:
        """
        self.__name = action_name
        self.__type = action_type

    @property
    def action_name(self):
        """
        返回动作的名称
        :return: name
        """
        return self.__name

    @action_name.setter
    def action_name(self, action_name: str):
        """
        更新动作的名称
        :param action_name: 动作的名称
        :return: None
        """
        self.__name = action_name

    @property
    def action_type(self):
        """
        返回动作的类型
        :return: type
        """
        return self.__type

    @action_type.setter
    def action_type(self, action_type: ActionEnum):
        """
        更新动作的类型
        :param action_type:
        :return:
        """
        self.__type = action_type
